from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import startup_db, shutdown_db
from app.routers.categoria import categoria_routers
from app.routers.turmas import turma_routers
from app.routers.funcionario import funcionario_router

app = FastAPI(title="Contador de Alunos")

app.add_event_handler(event_type='startup', func=startup_db)
app.add_event_handler(event_type='shutdown', func=shutdown_db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)

app.include_router(funcionario_router)
app.include_router(categoria_routers)
app.include_router(turma_routers)

@app.get("/")
async def status():
    return {"status": "ok"}