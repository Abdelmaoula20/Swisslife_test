from app.models.classification_models import (
    ClassificationRequest,
    
)
import time
from collections import Counter
from baml_client import b
from fastapi import HTTPException
from baml_py.internal_monkeypatch import BamlValidationError
import asyncio
import logging
logger = logging.getLogger(__name__)

async def classify_text(request: ClassificationRequest):

    NUM_RUNS = 5
    start_time = time.time()

    async def single_run():
        return await b.ClassifyText(
            text=request.text,
            themes=request.themes
        )

    try:
        # Run classifications in parallel
        results = await asyncio.gather(
            *[single_run() for _ in range(NUM_RUNS)]
        )

    except BamlValidationError:
        logger.error("LLM output parsing failed")
        raise HTTPException(
            status_code=500,
            detail="LLM output parsing failed"
        )

    except BamlError:
        logger.error("LLM service unavailable")
        raise HTTPException(
            status_code=503,
            detail="LLM service unavailable"
        )

    # Count votes
    votes = [r.chosen_theme.title for r in results]
    vote_counts = Counter(votes)

    chosen_title, count = vote_counts.most_common(1)[0]
    confidence = round(count / NUM_RUNS, 2)

    matching_theme = next(
        (t for t in request.themes if t.title == chosen_title),
        None
    )

    if not matching_theme:
        raise HTTPException(
            status_code=422,
            detail="Model returned a theme not present in provided themes"
        )

    duration = round(time.time() - start_time, 3)

    logger.info(
        f"Probabilistic classification | theme={chosen_title} | confidence={confidence} | duration={duration}s"
    )

    return {
        "model_reasoning": results[0].model_reasoning,
        "chosen_theme": matching_theme,
        "confidence": confidence
    }