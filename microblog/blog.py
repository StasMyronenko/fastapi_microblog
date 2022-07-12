from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from microblog.schemas import PostCreate, PostList

from . import service
from core.utils import get_db

router = APIRouter()


@router.get("/", response_model=List[PostList])
def post_list(db: Session = Depends(get_db)):
    return service.get_post_list(db)


@router.post("/")
def create_post(item: PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db, item)
