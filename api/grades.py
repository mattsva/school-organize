from fastapi import APIRouter
from database import crud

router = APIRouter()

@router.post("/")
def set_grade(user_uuid: str, subject: str, grade: float):
    return {"success": crud.set_grade(user_uuid, subject, grade)}
