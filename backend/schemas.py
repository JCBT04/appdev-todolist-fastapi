from pydantic import BaseModel
from typing import Optional

# Task schema used to create a new task
class TaskCreate(BaseModel):
    title: str
    completed: bool = False

# Task schema for reading a task (response model)
class TaskBase(TaskCreate):
    id: int

    class Config:
        orm_mode = True

# Task schema used for updating an existing task
class TaskUpdate(BaseModel):
    title: Optional[str]
    completed: Optional[bool]
