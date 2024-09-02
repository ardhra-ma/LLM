from app.models.intent_classifier import IntentClassifier
from app.core.config import ConfigLoader

class ValidationService:
    def __init__(self, config_loader: ConfigLoader):
        self.config_loader = config_loader

    def validate(self, client_id: str, query: str) -> str:
        client_config = self.config_loader.load_config(client_id)
        classifier = IntentClassifier(client_config["intents"])
        return classifier.classify(query)
