from nltk.corpus import wordnet
from typing import List

class IntentClassifier:
    def __init__(self, intents: List[str]):
        self.intents = intents

    def classify(self, query: str) -> str:
        for intent in self.intents:
            if self._is_match(intent, query):
                return intent
        return "Unknown"

    def _is_match(self, intent: str, query: str) -> bool:
        synonyms = set()
        for syn in wordnet.synsets(intent):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().lower())
        for word in query.lower().split():
            if word in synonyms:
                return True
        return False
