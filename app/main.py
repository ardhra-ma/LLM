import nltk
from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router

# Download the WordNet data
nltk.download('wordnet')

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

