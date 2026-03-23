from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    openai_api_key: str
    openai_model_name: str = "gpt-4o-mini"
    weather_api_key: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


config = Config()
