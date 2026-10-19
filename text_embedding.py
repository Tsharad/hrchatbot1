import os
from dotenv import load_dotenv
load_dotenv()
from openai import AzureOpenAI
def get_embedding(text):
    endpoint = "https://umesh-mlubxbd0-eastus2.cognitiveservices.azure.com/"
    model_name = "text-embedding-3-small"
    deployment = "text-embedding-3-small"
    AZURE_OPENAI_KEY = os.environ["AZURE_OPENAI_KEY"]
    api_version = "2024-02-01"

    client = AzureOpenAI(
        api_version="2024-12-01-preview",
        azure_deployment = deployment,
        azure_endpoint=endpoint,
        api_key=AZURE_OPENAI_KEY
    )

    response = client.embeddings.create(
        input=[text],
        model=deployment
    )

    return response.data[0].embedding


if __name__ == "__main__":
    text = "What are the leave policies?"
    embedding = get_embedding(text)
    print(embedding)