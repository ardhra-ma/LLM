import json

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path

    def load_config(self, client_id: str) -> dict:
        with open(self.config_path, 'r') as file:
            config = json.load(file)
        return config.get(client_id, {})
