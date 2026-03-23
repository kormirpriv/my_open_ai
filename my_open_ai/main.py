from my_open_ai.config import config
from my_open_ai.utils import get_embedding, cosine_similarity, get_embedding_with_retry
import openai
import numpy as np

# 1️⃣ Set API KEY
openai.api_key = config.openai_api_key

# 2️⃣ Documents
documents = [
    "Rekuperator Wanas 430 ma sprawność 85% przy niskich prędkościach",
    "Rekuperator Wanas ma moc 1000W"
]

# 3️⃣ Embedding of documents
doc_embeddings = [get_embedding_with_retry(doc) for doc in documents]

# 4️⃣ Embedding os question
query = "Jaką sprawność ma rekuperator Wanas 430"
query_emb = get_embedding(query)

# 5️⃣ cosine_similarity
similarities = [cosine_similarity(query_emb, doc_emb) for doc_emb in doc_embeddings]

# 6️⃣ The best document
best_doc = documents[np.argmax(similarities)]
print("Najbardziej podobny dokument:", best_doc)
