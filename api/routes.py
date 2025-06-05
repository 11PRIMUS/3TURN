from fastapi import FastAPI

router=APIRouter()

@router.get("/status")
def get_status():
    return {"status":"operational"}