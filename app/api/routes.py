# app/routes/generator.py
from app.api.endpoints import post_generator
from fastapi import APIRouter



api_router=APIRouter()

api_router.include_router(post_generator.router, prefix="/api", tags=["api"])