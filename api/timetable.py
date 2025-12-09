from fastapi import APIRouter
from database import crud

router = APIRouter()

@router.get("/{uuid}")
def get_timetable(uuid: str):
    return crud.build_timetable(uuid)
