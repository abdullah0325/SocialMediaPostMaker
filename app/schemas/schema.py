from pydantic import BaseModel
from typing import List

class PostRequest(BaseModel):
    platforms: List[str]
    hashtags: List[str]
    keywords: List[str]
    title: str

class PostResponse(BaseModel):
    platform: str
    post_text: str
    image_prompt: str
    image_url: str