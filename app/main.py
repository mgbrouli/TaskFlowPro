from app.routers import auth
from fastapi import FastAPI


app = FastAPI(title="TaskFlow Pro", version="1.0.0")

app.include_router(auth.router)


@app.get("/")
def reat_root():
    return {"message": "Bem-vindo ao TaskFLow Pro! API rodando com sucesso!"}