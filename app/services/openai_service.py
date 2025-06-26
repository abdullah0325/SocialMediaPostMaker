# app/services/openai_service.py

from langchain_openai import ChatOpenAI
from openai import OpenAI
from app.core.config import settings

llm = ChatOpenAI(
    model_name='gpt-4o-mini',
    api_key=settings.OPENAI_API_KEY,
    temperature=0
)

dalle_client = OpenAI(api_key=settings.OPENAI_API_KEY)
