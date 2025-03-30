from app.core.config.config import settings
from app.routes import item_routes
from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title=settings.app_name,
    description="A structured REST CRUD API built with FastAPI",
    version="1.0.0"
)

app.include_router(
    item_routes.router,
    prefix=settings.api_v1_prefix
)

@app.get("/")
async def root():
    return {"message": "Welcome to the CRUD API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)