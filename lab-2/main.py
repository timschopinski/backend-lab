from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import json
import os

app = FastAPI()

TASKS_FILE = "tasks.json"


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


def read_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def write_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1


@app.get("/health")
def get_health():
    return {
        "status": "OK",
        "timestamp": datetime.now().isoformat() + "Z"
    }


@app.get("/tasks")
def get_tasks():
    return read_tasks()


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    tasks = read_tasks()
    new_task = {
        "id": get_next_id(tasks),
        "title": task.title,
        "description": task.description,
        "completed": False,
        "createdAt": datetime.now().isoformat() + "Z"
    }
    tasks.append(new_task)
    write_tasks(tasks)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    tasks = read_tasks()
    task_index = next((i for i, t in enumerate(tasks) if t['id'] == task_id), None)
    
    if task_index is None:
        raise HTTPException(status_code=404, detail={"error": "Task not found", "id": task_id})
    
    task = tasks[task_index]
    
    if task_update.title is not None:
        task['title'] = task_update.title
    if task_update.description is not None:
        task['description'] = task_update.description
    if task_update.completed is not None:
        task['completed'] = task_update.completed
    
    task['updatedAt'] = datetime.now().isoformat() + "Z"
    
    tasks[task_index] = task
    write_tasks(tasks)
    
    return task
