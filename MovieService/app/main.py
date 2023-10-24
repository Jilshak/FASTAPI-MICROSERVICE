from fastapi import FastAPI
from api.movies import router as movie_router
from api.db import SessionLocal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



origins = [
    "http://localhost:8001",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie_router)

async def connect_to_db():
    db = SessionLocal()
    app.state.db = db

async def close_db_connection():
    db = app.state.db
    db.close()

app.add_event_handler("startup", connect_to_db)
app.add_event_handler("shutdown", close_db_connection)
