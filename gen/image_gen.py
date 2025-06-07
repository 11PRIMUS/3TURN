from pathlib import Path
from typing import Optional
from config import TEXT_TO_IMAGE_APP, IMAGES_DIR
import base64
import time
import logging

logger=logging.getLogger(__name__)

class Image_gen:
    def __init__(self, stub):
        self.stub=stub
        self.app_id = TEXT_TO_IMAGE_APP

    def generate(self, prompt:str) -> Optional[str]:
        """generate image from text prompt"""
        try:
            logger.info(f"generating image: {prompt[:50]}")
            result=self.stub.call(
                self.app_id,
                {'prompt': prompt},
                'super-user'
            )
            if 'result' not in result :
                logger.error("no result")
                return None
            return self._save_image(result['result'])
        
        except Exception as e:
            logger.error(f"image gen failed: {e}")
            return None
    
    def save_img(self, image_data)-> str:
        """save image data to file"""
        timestamp=int(time.time())
        image_path=IMAGES_DIR/ f"img_{timestamp}.png"
        #dif format
        if isinstance(image_data,str):
            image_bytes=base64.b64decode(image_data)

        else:
            image_bytes = image_data
        with open(image_path, 'wb') as f:
            f.write(image_bytes)

        logger.info(f"image saved: {image_path}")
        return str(image_path)
        