from fastapi import APIRouter, Depends, HTTPException
from app.schemas import TaskResponse, TaskCreate, TaskUpdate
from app.database import get_db
from sqlalchemy.orm import Session
from typing import Optional
from app.models import TaskEnum, Task



router = APIRouter(prefix='/tasks',
                   tags=["Tasks"])



@router.get("", response_model=list[TaskResponse])
def get_tasks(status: Optional[TaskEnum]= None, db: Session = Depends(get_db)):
    query = db.query(Task)
    if status is not None:
        query = query.filter(Task.status == status.value)
    task = query.all()
    return task

@router.post("", response_model=TaskResponse)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Not Found")
    update_data = task.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing_task, key, value)

    db.commit()
    db.refresh(existing_task)
    return existing_task

@router.get("/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="suka net tut nihuya")
    return existing_task

@router.delete("/{task_id}", status_code=204)
def delete_task_by_id(task_id: int, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="suka net tut nihuya")
    db.delete(existing_task)
    db.commit()
    db.refresh(existing_task)
    return None