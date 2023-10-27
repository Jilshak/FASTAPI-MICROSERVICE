import replicate
from decouple import config

replicate_api_key = config('REPLICATE_API_KEY')

print(replicate_api_key)

replicate.run(
    "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
    input={"prompt": "a 19th century portrait of a wombat gentleman"}
)
