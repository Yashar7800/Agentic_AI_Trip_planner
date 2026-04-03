from utils.config_loader import load_config


class ConfigLoader:
    def __init__(self):
        print(f"Loading Configs...")
        self.config = load_config()

    def __getitem__(self, items):
        return self.config[items]
    


config = ConfigLoader()
print(config['llm']['groq']['provider'])