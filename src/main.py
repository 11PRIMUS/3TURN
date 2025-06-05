from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    yield

def create_app() -> FastAPI:
    app=FastAPI( title=settings.app_name, version=settings.app_version, lifespan=lifespan)

    app.add_middleware(CORSMiddleware, ..)
    
    app.include_router(api_router,prefix="/api/1")  
    return app
app=create_app()