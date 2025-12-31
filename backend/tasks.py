from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import mydb, mycursor

router = APIRouter()

class Task(BaseModel):
    user_id: int
    title: str
    description: str = ""

# Add task
@router.post("/tasks")
def add_task(task: Task):
    mycursor.execute("INSERT INTO tasks (user_id, title, description) VALUES (%s, %s, %s)", 
                     (task.user_id, task.title, task.description))
    mydb.commit()
    return {"message": "Task added successfully"}

# Get tasks for user
@router.get("/tasks/{user_id}")
def get_tasks(user_id: int):
    mycursor.execute("SELECT id, title, description FROM tasks WHERE user_id=%s", (user_id,))
    tasks = mycursor.fetchall()
    return {"tasks": [{"id": t[0], "title": t[1], "description": t[2]} for t in tasks]}

# Update task
@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    mycursor.execute("UPDATE tasks SET title=%s, description=%s WHERE id=%s", 
                     (task.title, task.description, task_id))
    mydb.commit()
    return {"message": "Task updated successfully"}

# Delete task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    mycursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    mydb.commit()
    return {"message": "Task deleted successfully"}
