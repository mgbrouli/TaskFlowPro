from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate, TaskResponse
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tasks", tags=["Tarefas"])

@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks

@router.post("/", response_model=TaskCreate, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_task = Task(title= task_data.title,
                    description= task_data.description,
                    user_id = current_user.id,
                    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task