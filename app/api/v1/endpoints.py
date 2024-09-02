from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.core.config import ConfigLoader
from app.models.intent_classifier import IntentClassifier

router = APIRouter()

# Initialize ConfigLoader with the path to config.json
config_loader = ConfigLoader(r"C:\Users\286114\LLM_Intent_Validation\config.json")

class Query(BaseModel):
    client_id: str
    query: str

class IntentResponse(BaseModel):
    query: str
    intent: str
    description: str

class ClientConfig(BaseModel):
    client_name: str
    intents: List[str]

@router.post("/validate_intent", response_model=IntentResponse)
async def validate_intent(query: Query):
    client_config = config_loader.load_config(query.client_id)
    client_intents = client_config.get("intents")
    intent_descriptions = config_loader.load_config("intent_descriptions")
    
    if not client_intents:
        raise HTTPException(status_code=404, detail="Client not found")
    
    classifier = IntentClassifier(client_intents)
    intent = classifier.classify(query.query)
    description = intent_descriptions.get(intent, "No description available")
    
    return IntentResponse(query=query.query, intent=intent, description=description)

@router.post("/configure-client")
async def configure_client(config: ClientConfig):
    if config.client_name in config_loader.load_config("intent_schema"):
        raise HTTPException(status_code=400, detail="Client already exists")
    intent_schema = config_loader.load_config("intent_schema")
    intent_schema[config.client_name] = config.intents
    # Save the updated intent schema back to the config file if needed
    return {"message": "Client configured successfully"}

@router.get("/get-intents")
async def get_intents(client: str):
    client_config = config_loader.load_config(client)
    intents = client_config.get("intents")
    if not intents:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"client": client, "intents": intents}
