from prompt_up import upgrade
from gen.image_gen import Image_gen
from gen.gen_3d import gen_3dmodel
from typing import Dict, Any, Optional
import time

class create_pipeline:
    def __init__(self, stub, user_config):
        self.image_gen= Image_gen(stub)
        self.model_gen= gen_3dmodel(stub)
        self.config =user_config

    def process(self, user_prompt:str, context:Optional[Dict[str,Any]]=None)-> Dict[str, Any]:
        if context is None:
            context={'similar_creations':[]}

        enhanced_prompt=upgrade(user_prompt, context)
        image_path = self.image_gen.generate(enhanced_prompt)

        if not image_path:
            return self.err_response("3d gen failed", user_prompt, enhanced_prompt, image_path)
        
        model_path = self.model_gen.generate(enhanced_prompt, image_path)
        creation_id ="placeholder_id"
        
        metadata={
            'processing_time':time.time(),
            'has_context':len(context['similar_creations']) > 0

        }

        return {
            'success':True,
            'creation_id': creation_id,
            'original_prompt': user_prompt,
            'enhanced_prompt': enhanced_prompt,
            'image_path': image_path,
            'model_path': model_path,
            'similar_found': len(context['similar_creations']),
            'metadata': metadata
        }
    def err_response(self, error:str, original:str, ehnaced: str,image_path:str =None)-> Dict[str, Any]:
        return{
            'success': False,
            'error': error,
            'original_prompt': original,
            'enhanced_prompt': ehnaced,
            'image_path': image_path
        }
        

