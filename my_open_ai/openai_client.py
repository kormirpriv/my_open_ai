from openai import OpenAI

from my_open_ai.config import config

client = OpenAI(api_key=config.openai_api_key)
