# app/utils/content_utils.py

from langchain.prompts.chat import ChatPromptTemplate
from app.services.openai_service import llm, dalle_client
from app.utils.logger import logger


def generate_text(platform: str, hashtags: list, keywords: list, title: str):
    prompt_template = ChatPromptTemplate.from_template(
        "Create a social media post for {platform} about '{title}' using hashtags {hashtags} and keywords {keywords}."
    )

    formatted_prompt = prompt_template.format_messages(
        platform=platform,
        title=title,
        hashtags=", ".join(hashtags),
        keywords=", ".join(keywords)
    )

    logger.info(f"Generating post for {platform}")
    response = llm.invoke(formatted_prompt)
    post_text = getattr(response, 'content', str(response))
    image_prompt = extract_image_prompt_from_post(post_text)
    return post_text, image_prompt


def extract_image_prompt_from_post(post_text: str):
    prompt_template = ChatPromptTemplate.from_template(
        "Based on this social media post: \"{post}\", create a single, clear image prompt for DALL-E 3. "
        "The prompt should describe a single image related to PIAIC admissions being open. "
        "Return ONLY the prompt."
    )
    formatted_prompt = prompt_template.format_messages(post=post_text)
    response = llm.invoke(formatted_prompt)
    return getattr(response, 'content', str(response)).strip()


def generate_image(prompt: str):
    prompt = str(prompt).strip().replace('\n', ' ')
    if len(prompt) > 1000:
        prompt = prompt[:997] + "..."

    logger.info(f"Sending prompt to DALL-E: {prompt[:100]}...")
    response = dalle_client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality="standard"
    )
    return response.data[0].url
