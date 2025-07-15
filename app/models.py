from pydantic import BaseModel, Field, validator
from typing import Optional

class PostBase(BaseModel):
    title: str = Field(..., min_length=5)
    content: str
    author: Optional[str] = "Anonymous"

    @validator('title')
    def title_min_length(cls, v):
        if len(v) < 5:
            raise ValueError("Title must be at least 5 characters long")
        return v

class Post(PostBase):
    id: int
    createdAt: str
