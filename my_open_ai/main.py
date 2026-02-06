from my_open_ai.config import config
from my_open_ai.utils import get_embedding, cosine_similarity
import openai
import numpy as np

# 1️⃣ Ustaw klucz API z config
openai.api_key = config.openai_api_key

# 2️⃣ Przykładowe dokumenty
documents = [
    "Ala ma kota",
    "Ela ma psa"
]

# 3️⃣ Embedding dokumentów
doc_embeddings = [get_embedding(doc) for doc in documents]

# 4️⃣ Embedding pytania
query = "Co ma Ala?"
query_emb = get_embedding(query)

# 5️⃣ Oblicz podobieństwo kosinusowe
similarities = [cosine_similarity(query_emb, doc_emb) for doc_emb in doc_embeddings]

# 6️⃣ Wybierz najlepszy dokument
best_doc = documents[np.argmax(similarities)]
print("Najbardziej podobny dokument:", best_doc)