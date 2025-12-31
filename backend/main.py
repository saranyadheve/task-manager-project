from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Task
from pydantic import BaseModel

SECRET_KEY = "secret123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users_db = []
tasks_db = []  

# -------------------- Models --------------------
class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Task(BaseModel):
    title: str

# -------------------- Utils --------------------
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# -------------------- Auth Routes --------------------
@app.post("/register")
def register(user: UserRegister):
    for u in users_db:
        if u["username"] == user.username:
            raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = hash_password(user.password)
    users_db.append({"username": user.username, "password": hashed_password})
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: UserLogin):
    for u in users_db:
        if u["username"] == user.username and verify_password(user.password, u["password"]):
            access_token = create_access_token(data={"sub": user.username})
            return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# -------------------- Task Routes --------------------
@app.post("/tasks")
def add_task(task: Task, current_user: str = Depends(get_current_user)):
    tasks_db.append({"title": task.title, "user": current_user})
    return {"message": "Task added successfully"}

@app.get("/tasks")
def get_tasks(current_user: str = Depends(get_current_user)):
    user_tasks = [t for t in tasks_db if t["user"] == current_user]
    return {"tasks": user_tasks}

@app.delete("/tasks/{index}")
def delete_task(index: int, current_user: str = Depends(get_current_user)):
    user_tasks = [t for t in tasks_db if t["user"] == current_user]
    if index < 0 or index >= len(user_tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    real_index = tasks_db.index(user_tasks[index])
    tasks_db.pop(real_index)
    return {"message": "Task deleted"}

@app.put("/tasks/{index}")
def update_task(index: int, task: Task, current_user: str = Depends(get_current_user)):
    user_tasks = [t for t in tasks_db if t["user"] == current_user]
    if index < 0 or index >= len(user_tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    real_index = tasks_db.index(user_tasks[index])
    tasks_db[real_index]["title"] = task.title
    return {"message": "Task updated"}
