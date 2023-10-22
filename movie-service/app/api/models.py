from pydantic import BaseModel

class Movie(BaseModel):
    name: str
    plot: str
    genres: list[str]
    casts: list[str]