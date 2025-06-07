from pathlib import Path
from typing import Optional
from config import IMAGE_TO_3D_APP, MODELS_DIR
import base64
import time

class gen_3d:
    def __init__(self,stub):
        self.stub=stub
        self.app_id = IMAGE_TO_3D_APP
    
    def generate(self, image_path: str)-> Optional[str]:
        try:
            image_data = self._read_image(image_path)
            if not image_data:
                return None
            
            result = self.stub.call(
                self.app_id,
                {'image': image_data},
                'super-user'
            )

            if 'result' not in result:
                return None
            return self._save_model(result['result'])
        
        except Exception as e:
            return None
    
    def read_iamge(self, path: str) -> Optional[bytes]:
        try:
            with open(path, 'rb') as f:
                return f.read()
        except Exception as e:
            return None
    
    def save_mode(self, model_data) -> str:
        timestamp = int(time.time())
        model_path = MODELS_DIR / f"model_{timestamp}.obj"

        if isinstance(model_data, str):
            model_bytes=base64.b64decode(model_data)

        else:
            model_bytes=model_data

        with open(model_path, 'wb') as f:
            f.write(model_bytes)

        return str(model_path)