import os
import json
from openai import OpenAI
from dotenv import load_dotenv

from scraper import fetch_website_contents
load_dotenv()

system_prompts=""" You analyze the content of a website and provide a concise summary. ignore navigation menus, respond in markdown format, and focus on the main content. """

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_BASE_URL")
)       

def summarize(url):
    website=fetch_website_contents(url)
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompts},
            {"role": "user", "content": f"Summarize the following website content:\n\n{website}"}
        ]
    )
    return response.choices[0].message.content.strip()
