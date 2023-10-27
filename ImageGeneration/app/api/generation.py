import replicate
from dotenv import load_dotenv
from .models import GenerationBase
from fastapi import APIRouter, Body

load_dotenv()


generation = APIRouter()



@generation.post('/')
async def generate_prompt(prompt: str):
    output = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input= {'prompt': prompt}
    )
    return output
