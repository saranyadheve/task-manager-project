from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)


class RegisterModel(BaseModel):
    username: str
    password: str

class LoginModel(BaseModel):
    username: str
    password: str

class TaskModel(BaseModel):
    title: str
    description: str
    
class User(BaseModel):
    username: str
    password: str

# Task
class Task(BaseModel):
    title: str
    description: str
    status: str = "pending"
