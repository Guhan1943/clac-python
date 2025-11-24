from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_db():
    return sqlite3.connect("users.db")


@app.get("/user/{username}")
def get_user(username: str):
    conn = get_db()
    
    # ❌ VULNERABLE: Building SQL query using string concatenation
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    result = conn.execute(query).fetchone()
    conn.close()
    
    return {"user": result}
