# routes/classification.py

from fastapi import APIRouter
from app.models.classification_models import ClassificationRequest
from app.services.classification_service import classify_text

router = APIRouter()


@router.post("/classify")
async def classify(request: ClassificationRequest):
    return await classify_text(request)