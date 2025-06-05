import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name:str="model base pipeline"
    debug:bool =False

    class config:
        env_file=".env"

settings=Settings()