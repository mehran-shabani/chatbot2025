
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # Database URL
    DATABASE_URL: str = "postgresql://user:password@localhost/chatbot_db"

    # Redis URL for Celery
    REDIS_URL: str = "redis://localhost:6379/0"

    # OpenAI API Key
    OPENAI_API_KEY: str = "your_openai_api_key_here"

    # Kavenegar API Key for OTP
    KAVENEGAR_API_KEY: str = "your_kavenegar_api_key_here"

    class Config:
        # This tells pydantic to load variables from a .env file
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Create a single instance of the settings to be used throughout the application
settings = Settings()
