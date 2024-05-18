from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

host = os.getenv("MARIADB_HOST")
user = os.getenv("MARIADB_USER")
password = os.getenv("MARIADB_PASSWORD")
database = os.getenv("MARIADB_DATABASE")

db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = db.cursor()

@app.get("/")
def read_root():
    return {"message": user}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user[0], "name": user[1], "email": user[2]}

@app.post("/users/")
def create_user(name: str, email: str):
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    db.commit()
    return {"message": "User created successfully"}
