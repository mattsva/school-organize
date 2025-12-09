from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Dict, List
from database import crud

router = APIRouter()

class StudioTimeData(BaseModel):
    name: str
    teacher_uuids: Optional[List[int]] = []
    times: Optional[Dict] = {}

class StudioTimeEdit(BaseModel):
    new_name: Optional[str]
    teacher_uuids: Optional[List[int]]
    times: Optional[Dict]

@router.post("/create")
def create_studiotime(data: StudioTimeData):
    return crud.create_studiotime(data.name, data.teacher_uuids, data.times)

@router.put("/edit/{name}")
def edit_studiotime(name: str, data: StudioTimeEdit):
    return crud.edit_studiotime(name, data.new_name, data.teacher_uuids, data.times)

@router.delete("/delete")
def delete_studiotime(name: str):
    return crud.delete_studiotime(name)

@router.get("/list")
def list_studiotimes():
    return crud.list_studiotimes()

@router.post("/book")
def book_studiotime(user_uuid: int, studiostime_name: str):
    return crud.book_studiotime(user_uuid, studiostime_name)

@router.post("/unbook")
def unbook_studiotime(user_uuid: int, studiostime_name: str):
    return crud.unbook_studiotime(user_uuid, studiostime_name)
