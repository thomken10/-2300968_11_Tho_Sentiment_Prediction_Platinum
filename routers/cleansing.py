from fastapi import APIRouter
from fastapi import Query
from services.cleansing import file_cleansing

router = APIRouter()

@router.get("/cleansing")
async def text_cleansing(sentence: str = Query(default="")):
    
    result= await file_cleansing(sentence)
    return result
