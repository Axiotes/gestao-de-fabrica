from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def connect():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="",
        database="projeto"
    )

@app.post("/login")
async def validate_login(
    email: str = Form(...),
    senha: str = Form(...)
):
    conn = connect()
    cursor = conn.cursor()
    comando = f"""SELECT * FROM users WHERE email = '{email}' and senha = md5('{senha}')"""
    data = cursor.execute(comando)
    records = cursor.fetchall()

    if records == []:
        return False
    else:
        return True