from fastapi import APIRouter, Depends, HTTPException
from app.oauth2 import get_current_user
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import TaskCreate, TaskResponse, TaskUpdate
from app.models import Task
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=List[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db), current_user: Task = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.owner_id == current_user.id).all()
    return tasks

@router.post("/create", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: Task = Depends(get_current_user)):
    new_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        due_date=task.due_date,
        priority=task.priority,
        owner_id=current_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: Task = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: Task = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if current_user.id != task.owner_id:
        raise HTTPException(
            status_code=403,
            detail="it's not your account task, you can't delete this task"
        )
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db), current_user: Task = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if current_user.id != task.owner_id:
        raise HTTPException(status_code=403, detail="it's not your account task, you can't update this task")

    update_data = task_update.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task