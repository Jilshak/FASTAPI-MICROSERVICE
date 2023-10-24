from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from api.db import Base, SessionLocal
from pydantic import BaseModel


# this is the pydantic model for response and data validation
class UserBase(BaseModel):
    username: str
    hashed_password: str

# in this code i've added a the id to the movie_model 
class UserModel(UserBase):
    id: int

    class Config:
        orm_mode = True

# this is the original database schema
# the Base which is being extended here helps this model to map to the database
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    hashed_password = Column(String)
