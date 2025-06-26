from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.content_utils import generate_text, generate_image

router = APIRouter()

class PostRequest(BaseModel):
    platforms: list
    hashtags: list
    keywords: list
    title: str

@router.post("/generate-posts")
async def create_posts(request: PostRequest):
    try:
        posts = []
        for platform in request.platforms:
            text, image_prompt = generate_text(platform, request.hashtags, request.keywords, request.title)
            image_url = generate_image(image_prompt)
            posts.append({
                "platform": platform,
                "post_text": text,
                "image_prompt": image_prompt,
                "image_url": image_url
            })
        return {"status": "success", "data": posts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
