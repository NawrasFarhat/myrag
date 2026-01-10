from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWD_TYPE: list
    FILE_MAX_SIZE: int 
    FILE_DEFFAULT_CHUNK_SIZE: int
    
    MONGODB_URL: str
    MONGODB_DATABASE:str


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

def get_settings():
    return Settings()
