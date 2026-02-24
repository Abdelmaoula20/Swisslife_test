from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from app.routes.classification import router as classification_router
from app.routes.form import router as form_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)


app = FastAPI(title="Swiss Life AI Technical Test")


@app.on_event("startup")
async def validate_env():
    required_vars = ["OPENAI_API_KEY", "OPENAI_BASE_URL"]
    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        raise RuntimeError(f"Missing required environment variables: {missing}")


@app.get("/")
async def health_check():
    return {"message": "Swiss Life AI Test API running ..."}


app.include_router(classification_router)
app.include_router(form_router)