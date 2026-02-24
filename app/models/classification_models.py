from pydantic import BaseModel, Field
from typing import List
from typing import Optional

class ThemeModel(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

class ClassificationRequest(BaseModel):
    text: str = Field(..., min_length=1)
    themes: List[ThemeModel] = Field(..., min_items=1)
    confidence: Optional[float] = None



