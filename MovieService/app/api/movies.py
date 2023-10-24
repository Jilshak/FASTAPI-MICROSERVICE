from fastapi import APIRouter, Depends, HTTPException
import sys
sys.path.append('C:\\Users\\Jilshak\\Desktop\\FASTAPI-MICROSERVICE')
from sqlalchemy.orm import Session
from api.db import SessionLocal, engine, Base
from api.models import MovieResponse, MovieModel, MovieBase, get_db
from AuthenticationService.app.api.auth import get_current_user


router = APIRouter()

Base.metadata.create_all(bind=engine)


@router.get("/", response_model=list[MovieModel])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    movies = db.query(MovieResponse).offset(skip).limit(limit).all()
    return movies


@router.post('/', response_model=MovieModel)
def post_movie(movie: MovieBase, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    new_movie = MovieResponse(**movie.model_dump())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
