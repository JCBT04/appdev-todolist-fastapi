from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class TaskBase(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: Optional[str]
    completed: Optional[bool]
