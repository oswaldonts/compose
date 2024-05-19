from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = FastAPI()

host = os.getenv("MARIADB_HOST")
user = os.getenv("MARIADB_USER")
password = os.getenv("MARIADB_PASSWORD")
database = os.getenv("MARIADB_DATABASE")

while True:
    try:
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
           database=database
        )
        # db.close()
        break  # Salir del bucle si la conexión tiene éxito
    except mysql.connector.Error:
        print("Error: No se pudo conectar a la base de datos. Intentando nuevamente en 5 segundos...")
        time.sleep(5)



# db = mysql.connector.connect(
#     host=host,
#     user=user,
#     password=password,
#     database=database
# )

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
