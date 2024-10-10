from http.client import HTTPException

from fastapi import APIRouter

from app.models import TurmaDataBase, CategoriaDataBase
from app.schemas import TurmaCreate, TurmaRead, TurmaReadAll, TurmaUpdate

turma_routers = APIRouter(prefix="/turma", tags=["Turma"])

@turma_routers.get(path="/", response_model=TurmaReadAll)
def listar_todas_as_turmas():
    """Lista todas as turmas."""

    turmas = TurmaDataBase.select()

    return {'turmas': turmas}

@turma_routers.get(path="/{turma_id}", response_model=TurmaRead)
def listar_uma_turma(turma_id: int):
    """Retorna uma turma específica pelo ID."""

    turma = TurmaDataBase.get_or_none(id=turma_id)

    if turma is None:
        raise HTTPException(status_code=404, detail="Turma não encontrada")

    return turma


@turma_routers.post(path="/", response_model=TurmaRead)
def criar_turma(nova_turma: TurmaCreate):
    """Cria uma nova turma."""

    categoria = CategoriaDataBase.get_or_none(id=nova_turma.categoria_id)

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    turma = TurmaDataBase.create(
        nome=nova_turma.name,
        categoria=categoria
    )

    return turma


@turma_routers.put(path='/{turma_id}', response_model=TurmaRead)
def atualizar_turma(turma_id: int, turma_atualizada: TurmaUpdate):
    """Atualiza uma turma existente."""

    turma = TurmaDataBase.get_or_none(id=turma_id)

    if turma is None:
        raise HTTPException(status_code=404, detail="Turma não encontrada")

    turma.nome = turma_atualizada.nome

    turma.save()

    return turma

@turma_routers.delete(path='/{turma_id}', response_model=TurmaRead)
def deletar_turma(turma_id: int):
    """Deleta uma turma."""

    turma = TurmaDataBase.get_or_none(TurmaDataBase.id == turma_id)

    if turma is None:
        raise HTTPException(status_code=404, detail="Turma não encontrada")

    turma.delete()

    return turma

