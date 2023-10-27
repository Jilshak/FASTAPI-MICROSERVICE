from pydantic import BaseModel

class GenerationBase(BaseModel):
    prompt: str
    
    