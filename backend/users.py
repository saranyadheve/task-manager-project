from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import mydb, mycursor
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Request body schema
class User(BaseModel):
    username: str
    password: str

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Register
@router.post("/register")
def register(user: User):
    hashed_password = hash_password(user.password)

    try:
        mycursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (user.username, hashed_password)
        )
        mydb.commit()
        return {"message": "User registered successfully"}
    except Exception:
        raise HTTPException(status_code=400, detail="Username already exists")

# Login
@router.post("/login")
def login(user: User):
    mycursor.execute(
        "SELECT password FROM users WHERE username=%s",
        (user.username,)
    )
    result = mycursor.fetchone()

    if not result:
        raise HTTPException(status_code=400, detail="User not found")

    hashed_password = result[0]

    if verify_password(user.password, hashed_password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect password")
