from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from api.db import Base, SessionLocal
from pydantic import BaseModel


# this is the pydantic model for response and data validation
class MovieBase(BaseModel):
    title: str
    plot: str
    genres: str
    casts: str

# in this code i've added a the id to the movie_model 
class MovieModel(MovieBase):
    id: int

    class Config:
        orm_mode = True

# this is the original database schema
# the Base which is being extended here helps this model to map to the database
class MovieResponse(Base):
    __tablename__ = "movie_response"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    plot = Column(String)
    genres = Column(String)
    casts = Column(String)


# this is to connect to the db and do crud application
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()