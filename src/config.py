import os
from pydantic_settings import BaseSettings
from pathlib import Path

TEXT_TO_IMAGE_APP = 'f0997a01-d6d3-a5fe-53d8-561300318557'
IMAGE_TO_3D_APP = '69543f29-4d41-4afc-7f29-3d51591f11eb'

DB_NAME="creative_memory.db"

OUTPUT_DIR=Path("outputs")
IMAGES_DIR=OUTPUT_DIR/ "images"
MODELS_DIR=OUTPUT_DIR/"3d_model"

LOG_LEVEL="INFO"

def setup_dir():
    for dir_path in [OUTPUT_DIR, IMAGES_DIR, MODELS_DIR]:
        dir_path.mkdir(exist_ok=True)

