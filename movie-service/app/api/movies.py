from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.db import SessionLocal, engine, Base
from api.models import MovieResponse, MovieModel, MovieBase, get_db

router = APIRouter()

Base.metadata.create_all(bind=engine)

@router.get("/", response_model=list[MovieModel])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = db.query(MovieResponse).offset(skip).limit(limit).all()
    return movies


@router.post('/', response_model=MovieModel)
def post_movie(movie: MovieBase, db: Session = Depends(get_db)):
    new_movie = MovieResponse(**movie.model_dump())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
