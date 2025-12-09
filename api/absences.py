from fastapi import APIRouter
from database import crud
from datetime import date

router = APIRouter()

@router.post("/") # TODO: Add premission verification and a whole working system
def add_absence(user_uuid: str, day: date, status: str):
    return {"success": crud.add_absence(user_uuid, day, status)}