import time

import numpy as np
import openai
from openai import OpenAI, APIError, RateLimitError

from my_open_ai.config import config

client = OpenAI(api_key=config.openai_api_key)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Calculating cosine similarity for a and b."""
    cos_similarity = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    print(f"Cosine_similarity: {cos_similarity}")
    return cos_similarity


def get_embedding(text: str, model: str = "text-embedding-3-small") -> np.ndarray:
    """Creating embedding matrix using OpenAI."""
    response = client.embeddings.create(input=text, model=model)
    print(f"Embedding: {response.data[0].embedding}")
    return np.array(response.data[0].embedding)


def get_embedding_with_retry(text, model="text-embedding-3-small", max_retries=5):
    print("Using API key:", openai.api_key)
    last_error = None
    for i in range(max_retries):
        response = None
        try:
            response = client.embeddings.create(model=model, input=text)
            return np.array(response.data[0].embedding)
        except RateLimitError as e:
            wait = 2 ** i  # exponential backoff
            print(f"Rate limit, retrying in {wait} seconds...")
            time.sleep(wait)
            last_error = e
        except APIError as e:
            print(f"API error: {e}. Retrying...")
            time.sleep(2 ** i)
            last_error = e
    raise Exception("Exceeded maximum retries") from last_error
