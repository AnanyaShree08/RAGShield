from pydantic_settings import BaseSettings,  SettingsConfigDict
class Settings(BaseSettings):
    app_name: str = "RAGShield API"
    app_version: str = "1.0.0"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
