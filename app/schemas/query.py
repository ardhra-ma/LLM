from pydantic import BaseModel

class Query(BaseModel):
    client_id: str
    query: str

class IntentResponse(BaseModel):
    query: str
    intent: str
