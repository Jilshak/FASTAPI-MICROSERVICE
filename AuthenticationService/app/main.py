from fastapi import FastAPI, Depends, HTTPException, status
from api.db import Base, engine, SessionLocal
from api.models import UserBase, UserModel
from sqlalchemy.orm import Session
from api import auth
from typing import Annotated
from api.auth import get_current_user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)



origins = [
    "http://localhost:8000",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


user_dependency = Annotated[dict, Depends(get_current_user)]
db_dependency = Annotated[Session, Depends(get_db)]


@app.get('/', response_model=dict, status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    return {"user": user}
