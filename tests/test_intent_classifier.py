import unittest
from app.models.intent_classifier import IntentClassifier

class TestIntentClassifier(unittest.TestCase):
    def test_classify(self):
        intents = ["Information Request", "Action Request"]
        classifier = IntentClassifier(intents)
        self.assertEqual(classifier.classify("What time is it?"), "Information Request")
        self.assertEqual(classifier.classify("Please do this"), "Action Request")
        self.assertEqual(classifier.classify("Unknown query"), "Unknown")

if __name__ == '__main__':
    unittest.main()
