from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    API_V1_STR : str= '/api/v1'
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    
    class Config:
        env_file = ".env"

settings = Settings()