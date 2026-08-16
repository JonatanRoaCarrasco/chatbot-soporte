from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "Chatbot de Soporte"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/chatbot"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # LLM
    LLM_API_KEY: str = ""
    LLM_MODEL: str = "deepseek"
    
    # Vector Database
    VECTOR_DB_URL: str = "postgresql://user:password@localhost:5432/chatbot"
    
    class Config:
        env_file = ".env"

settings = Settings()
