from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.models import TaskEnum

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str] = None
    status: TaskEnum
    created_at: datetime

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskEnum] = None

    model_config= ConfigDict(
        extra='forbid',
    )