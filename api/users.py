from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from database import crud

router = APIRouter()

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    title: str

class UserEdit(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    title: Optional[str]

@router.post("/create")
def create_user(data: UserCreate):
    return crud.create_user(data.firstname, data.lastname, data.title)

@router.get("/list")
def list_users():
    return crud.list_users()

@router.get("/{user_uuid}")
def get_user(user_uuid: int):
    return crud.get_user(user_uuid)

@router.put("/edit/{user_uuid}")
def edit_user(user_uuid: int, data: UserEdit):
    return crud.edit_user(user_uuid, data.firstname, data.lastname, data.title)

@router.delete("/delete/{user_uuid}")
def delete_user(user_uuid: int):
    return crud.delete_user(user_uuid)

@router.get("/{user_uuid}/permissions")
def get_user_permissions(user_uuid: int):
    return crud.list_permissions(user_uuid)

@router.post("/{user_uuid}/grades")
class GradeData(BaseModel):
    subject: str
    grade: str

@router.post("/{user_uuid}/grades")
def set_grade(user_uuid: int, data: GradeData):
    return crud.set_grade(user_uuid, data.subject, data.grade)

class AbsenceData(BaseModel):
    date: str
    status: str

@router.post("/{user_uuid}/absences")
def add_absence(user_uuid: int, data: AbsenceData):
    return crud.add_absence(user_uuid, data.date, data.status)

@router.get("/{user_uuid}/timetable")
def get_timetable(user_uuid: int):
    return crud.build_timetable(user_uuid)