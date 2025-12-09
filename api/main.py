from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.users import router as users_router
from api.permissions import router as permissions_router
from api.courses import router as courses_router
from api.subjects import router as subjects_router
from api.studiots import router as studiots_router

app = FastAPI(title="School Management API")

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routs from files
app.include_router(users_router, prefix="/api/users", tags=["Users"])
app.include_router(permissions_router, prefix="/api/permissions", tags=["Permissions"])
app.include_router(courses_router, prefix="/api/courses", tags=["Courses"])
app.include_router(subjects_router, prefix="/api/subjects", tags=["Subjects"])
app.include_router(studiots_router, prefix="/api/studiots", tags=["StudioTimes"])
