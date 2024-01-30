from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector


app = FastAPI()

origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def connect():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='projeto'
    )

@app.post("/login")
async def validate_login(
    email: str = Form(...),
    senha: str = Form(...)
):
    try:
        comando = f"""SELECT * FROM users WHERE email = '{email}' and senha = md5('{senha}')"""
        conn = connect()
        cursor = conn.cursor()
        data = cursor.execute(comando)
        cursor.close()

        return data.fetchone()
    except mysql.connector.Error as err:

        return format(err)
