import yaml


class Config:
    def __init__(self, path="config.yaml"):
        with open(path, "r") as f:
            cfg = yaml.safe_load(f)
        self.openai_api_key = cfg["openai"]["api_key"]
        self.model_name = cfg["openai"].get("model", "gpt-4o-mini")


config = Config()
