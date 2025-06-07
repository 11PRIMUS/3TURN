from create import create_pipeline
from config import setup_dir, LOG_LEVEL
from openfabric_pysdk import configurations, Stub
import logging

logger=logging.getLogger(__name__)

def execute(model):
    setup_dir()
    request=model.request
    user_prompt=request.prompt

    user_config = configurations.get('super-user', None)
    logging.info(f"configuration: {configurations}")
    app_ids = user_config.app_ids if user_config else []
    stub = Stub(app_ids)

    try:
        pipline =create_pipeline(stub, user_config)
        result=pipline.process(user_prompt)
        if result['success']:
            message=format_success_msg(result)
        else:
            message=format_err_msg(result)

    except Exception as e:
        message=f"processing failed: {str(e)}"

    model.response.message=message

def format_success_msg(result):
    return f"""creation completed

Original: {result['original_prompt']}
Image: {result['image_path']}
3d_model: {result['model_path']}

found {result['similar_found']} similar creation .
your vision is now a 3D reality"""

def format_err_msg(result):
    return f""" generation failed
Prompt: {result['original_prompt']}
Error: {result['error']}

please try again."""