import logging
import os
from openai import OpenAI
from typing import Dict , List

logger= logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

client=OpenAI(
    base_url="https://api.studio.nebius.com/v1",
    api_key=os.getenv("NEBIUS_API_KEY")
)
def upgrade(user_prompt:str, history: List[str] =None)-> str :
    history_text ="\n".join (history or [])
    message= [
        {"role": "system", "content":(
            "You are creative assistant that enhances prompts for AI image generation."
            "your goal is to make user prompt more vivid, creative, cinematic and detaled, while keeping them grounded.")},
        {"role":"user","content":f"previos prompts: \n{history_text} \n\nNew prompt: \n{user_prompt}"}
    ]
    try :
        response = client.chat.completions.create(
            model="Qwen/Qwen3-4B-fast",
            temperature=0.6,
            top_p=0.95,
            messages=message
        )
        enhanced= response.choices[0].message.content
        logger.info("prompt enhanced using qwen")
        return enhanced.strip()
    except Exception as e:
        logger.warning(f"enhance failed")
        return f"a detailed scene featuring {user_prompt}."
    
def pre_context(prompt: str,history :List[str]) -> str:
    if not history:
        return prompt
    return f"{prompt} (in the theme of :{history[-1]})"
