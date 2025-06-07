from pathlib import Path
from typing import Optional
from config import TEXT_TO_IMAGE_APP, IMAGES_DIR
import base64
import time

class Image_gen:
    def __init__(self, stub):
        self.stub=stub
        self.app_id = TEXT_TO_IMAGE_APP

    def generate(self, prompt:str) -> Optional[str]:
        try:
            result=self.stub.call(
                self.app_id,
                {'prompt': prompt},
                'super-user'
            )
            if 'result' not in result :
                return None
            return self._save_image(result['result'])
        except Exception as e:
            return None
    
    def save_img(self, image_data)-> str:
        timestamp=int(time.time())
        image_path=IMAGES_DIR/ f"img_{timestamp}.png"
        #dif format
        if isinstance(image_data,str):
            image_bytes=base64.b64decode(image_data)

        else:
            image_bytes = image_data
        with open(image_path, 'wb') as f:
            f.write(image_bytes)

        return str(image_path)
        