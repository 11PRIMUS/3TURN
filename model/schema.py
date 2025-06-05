from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class gen_request(BaseModel):
    prompt:str=Field(...,min_length=1, max_length=500)
    user_id:str
    style:Optional[str]=None

class gen_response(BaseModel):
    request_id:str
    status:str
    message:str