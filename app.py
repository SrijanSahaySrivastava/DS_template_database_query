from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()


class User(BaseModel):
    name: str
    id: int


def add_user(user: User):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, id) VALUES (?, ?)", (user.name, user.id))
    conn.commit()
    conn.close()


@app.post("/adduser")
def add_user_api(user: User):
    add_user(user)
    return {"message": "User added successfully!"}
