from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Dict
from database import crud

router = APIRouter()

class CourseData(BaseModel):
    name: str
    teacher_uuid: int
    times: Optional[Dict] = {}

class CourseEdit(BaseModel):
    new_name: Optional[str]
    teacher_uuid: Optional[int]
    times: Optional[Dict]

@router.post("/create")
def create_course(data: CourseData):
    return crud.create_course(data.name, data.teacher_uuid, data.times)

@router.put("/edit/{name}")
def edit_course(name: str, data: CourseEdit):
    return crud.edit_course(name, data.new_name, data.times, data.teacher_uuid)

@router.delete("/delete")
def delete_course(name: str):
    return crud.delete_course(name)

@router.get("/list")
def list_courses():
    return crud.list_courses()

@router.post("/book")
def book_course(user_uuid: int, course_name: str):
    return crud.book_course(user_uuid, course_name)

@router.post("/unbook")
def unbook_course(user_uuid: int, course_name: str):
    return crud.unbook_course(user_uuid, course_name)
