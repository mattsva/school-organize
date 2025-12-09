from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Dict
from database import crud

router = APIRouter()

class SubjectData(BaseModel):
    name: str
    teacher_uuid: int
    times: Optional[Dict] = {}

class SubjectEdit(BaseModel):
    new_name: Optional[str]
    teacher_uuid: Optional[int]
    times: Optional[Dict]

@router.post("/create")
def create_subject(data: SubjectData):
    return crud.create_subject(data.name, data.teacher_uuid, data.times)

@router.put("/edit/{name}")
def edit_subject(name: str, data: SubjectEdit):
    return crud.edit_subject(name, data.new_name, data.teacher_uuid, data.times)

@router.delete("/delete")
def delete_subject(name: str):
    return crud.delete_subject(name)

@router.get("/list")
def list_subjects():
    return crud.list_subjects()

@router.post("/book")
def book_subject(user_uuid: int, subject_name: str):
    return crud.book_subject(user_uuid, subject_name)

@router.post("/unbook")
def unbook_subject(user_uuid: int, subject_name: str):
    return crud.unbook_subject(user_uuid, subject_name)
