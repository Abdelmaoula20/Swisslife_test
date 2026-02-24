from fastapi import APIRouter
from app.models.form_models import (
    FormCompletionRequest,
    FormCompletionResponse
)
from app.services.form_service import complete_form

router = APIRouter()


@router.post("/form-completion", response_model=FormCompletionResponse)
async def form_completion(request: FormCompletionRequest):
    return await complete_form(request)