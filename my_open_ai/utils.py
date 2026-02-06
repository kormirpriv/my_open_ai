import numpy as np
import openai


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Calculating cosine similarity for a and b."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_embedding(text: str, model: str = "text-embedding-3-small") -> np.ndarray:
    """Creating embedding matrix using OpenAI."""
    response = openai.embeddings.create(input=text, model=model)
    return np.array(response["data"][0]["embedding"])
