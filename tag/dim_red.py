from openai import OpenAI
import numpy as np
import pandas as pd

client = OpenAI(
    api_key= "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"
)

def normalize_l2(x):
    x = np.array(x)
    if x.ndim == 1:
        norm = np.linalg.norm(x)
        if norm == 0:
            return x
        return x / norm
    else:
        norm = np.linalg.norm(x, 2, axis=1, keepdims=True)
        return np.where(norm == 0, x, x / norm)

input_datapath = "tag/text.csv"
df = pd.read_csv(input_datapath)

response = client.embeddings.create(
    model="text-embedding-3-small", input=df, encoding_format="float"
)

cut_dim = response.data[0].embedding[:5]
norm_dim = normalize_l2(cut_dim)

print(norm_dim)