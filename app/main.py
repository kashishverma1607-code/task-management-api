from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Management API")

class Task(BaseModel):
    title: str
    completed: bool = False

tasks = []
next_id = 1

@app.get("/")
def home():
    return {"message": "Task Management API is running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    next_id += 1

    return new_task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
