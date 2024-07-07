import pandas as pd
import tiktoken

from openai import OpenAI
client = OpenAI(
    api_key= "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"
)

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

embedding_model = "text-embedding-3-small"
embedding_encoding = "cl100k_base"
max_tokens = 8000  # the maximum for text-embedding-3-small is 8191

# load & inspect dataset
input_datapath = "tag/text.csv"
df = pd.read_csv(input_datapath)
df = df[["Text"]]
df = df.dropna()
df["combined"] = (
    "Text: " + df.Text.str.strip()
)
df.head(2)

# Get embeddings and save for future
df["embedding"] = df.combined.apply(lambda x: get_embedding(x, model=embedding_model))
df.to_csv("tag/text_emb.csv")