import pandas as pd
from pandas import DataFrame as df
from openai import OpenAI

client = OpenAI(
    api_key= "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"
)

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

intro_data = pd.read_csv('tag/introduction.csv', sep=',', dtype=str)

df['ada_embedding'] = df.combined.apply(lambda x: get_embedding(x, model='text-embedding-3-small'))
df.to_csv('tag/introduction_output.csv', index=False)


# intro_data = pd.read_csv('tag/introduction.csv', sep=',', dtype=str)

# openai_embedding_model = "text-embedding-ada-002"

# def get_embedding(text: str, model: str) -> list[float]:
#     result = OpenAI.Embedding.create(
#       model=model,
#       input=text)
#     return result["data"][0]["embedding"]
    
# intro_data['openai_embeddings'] = intro_data['text'].apply(lambda x : get_embedding(x, openai_embedding_model))