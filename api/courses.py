from fastapi import APIRouter
from database import crud

router = APIRouter()

@router.post("/")
def create_course(name: str, teacher_uuid: str):
    return crud.create_course(name, teacher_uuid)

@router.delete("/{name}")
def delete_course(name: str):
    return {"success": crud.delete_course(name)}

@router.post("/book")
def book_course(user_uuid: str, course: str):
    return {"success": crud.book_course(user_uuid, course)}

@router.post("/unbook")
def unbook_course(user_uuid: str, course: str):
    return {"success": crud.unbook_course(user_uuid, course)}
