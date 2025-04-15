from models import Task
from schemas import TaskCreate, TaskUpdate
from sqlalchemy.orm import Session

# Create a new task
def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get all tasks (with optional filter)
def get_tasks(db: Session, filter_by: str = "all"):
    if filter_by == "completed":
        return db.query(Task).filter(Task.completed == True).all()
    elif filter_by == "pending":
        return db.query(Task).filter(Task.completed == False).all()
    return db.query(Task).all()

# Get a task by its ID
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# Update a task by ID
def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        if task.title is not None:
            db_task.title = task.title
        if task.completed is not None:
            db_task.completed = task.completed
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

# Delete a task by ID
def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    return None
