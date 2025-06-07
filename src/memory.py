from database import init_db, save_creation, get_recent_creation
from config import DB_NAME
from datetime import datetime
from typing import Dict, List
import logging

logger=logging.getLogger(__name__)

class memory_manager:
    def __init__(self):
        self.db_path= DB_NAME
        self.session_data={}
        self._setup()

    def _setup(self): #memory system init
        init_db(self.db_path)
        logger.info("memory system ready")

    def store(self, original_prompt:str, enhanced_prompt: str, image_path: str=None, model_3d_path: str=None, metadata: Dict=None) -> int:
        """store new creation"""
        creation_id=save_creation(self.db_path, original_prompt, enhanced_prompt, image_path, model_3d_path, metadata)

        self.session_data[creation_id]={ #updatesession memory
            'prompt': original_prompt,
            'enhanced': enhanced_prompt,
            'time': datetime.now().isoformat()

        }
        logger.info(f"stored creation id: {creation_id}")
        return creation_id
    
    def recall_similar(self, prompt:str, limit: int=5)->List[Dict]:
        """get similar creation if exists from memory"""
        #recent one
        return get_recent_creation(self.db_path, limit)
    
    def get_context(self, prompt: str)-> Dict:
        """context form prompt enhancement"""
        similar=self.recall_similar(prompt)
        return {
            'similaar_creation': similar,
            'session_history': self.session_data
        }
