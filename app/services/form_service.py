import asyncio
import time
import logging
from fastapi import HTTPException
from baml_client import b
from baml_py.errors import BamlError, BamlValidationError
from app.models.form_models import FormCompletionRequest

logger = logging.getLogger(__name__)


def validate_form_consistency(result):
    """
    Business-level validation.
    Ensures logical consistency between extracted fields.
    """

    # Email preferred but no email provided
    if (
        result.contact_info.preferred_contact_method == "Email"
        and not result.contact_info.email
    ):
        logger.warning("Inconsistent data: preferred contact is Email but email is missing")
        raise HTTPException(
            status_code=422,
            detail="Preferred contact method is Email but no email address provided"
        )

    # Phone preferred but no phone provided
    if (
        result.contact_info.preferred_contact_method == "Phone"
        and not result.contact_info.phone
    ):
        logger.warning("Inconsistent data: preferred contact is Phone but phone is missing")
        raise HTTPException(
            status_code=422,
            detail="Preferred contact method is Phone but no phone number provided"
        )

    # Empty call_reasons list should be null
    if result.contact_info.call_reasons == []:
        result.contact_info.call_reasons = None


async def complete_form(request: FormCompletionRequest):

    MAX_RETRIES = 3
    start_time = time.time()

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.info(f"Form LLM attempt {attempt}")

            result = await b.CompleteForm(
                text=request.text
            )

            break

        except BamlValidationError:
            logger.error("Form parsing failed")
            raise HTTPException(
                status_code=500,
                detail="LLM output parsing failed"
            )

        except BamlError:
            logger.warning(f"Form LLM error on attempt {attempt}")

            if attempt == MAX_RETRIES:
                raise HTTPException(
                    status_code=503,
                    detail="LLM service unavailable"
                )

            await asyncio.sleep(attempt)

    # Business validation layer
    validate_form_consistency(result)

    duration = round(time.time() - start_time, 3)

    logger.info(
        f"Form completion completed | duration={duration}s"
    )

    return result