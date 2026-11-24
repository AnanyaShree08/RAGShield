from pydantic_settings import BaseSettings,  SettingsConfigDict
class Settings(BaseSettings):
    app_name: str = "RAGShield API"
    app_version: str = "1.0.0"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env")
    


settings = Settings()
