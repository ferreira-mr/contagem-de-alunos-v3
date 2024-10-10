from fastapi import APIRouter, HTTPException

from app.schemas import FuncionarioReadAll, FuncionarioCreate, FuncionarioUpdate, FuncionarioReadOne
from app.models import FuncionarioDataBase

funcionario_router = APIRouter(prefix="/funcionario", tags=["Funcionário"])


@funcionario_router.get(path="/", response_model=FuncionarioReadAll)
def listar_todos_os_funcionarios():
    """Lista todos os funcionarios"""

    funcionarios = FuncionarioDataBase.select()

    return {'funcionarios': funcionarios}

@funcionario_router.get(path="/{funcionario_id}", response_model=FuncionarioReadOne)
def listar_um_funcionario(funcionario_id):
    """Lista um funcionario"""

    funcionario = FuncionarioDataBase.get_or_none(FuncionarioDataBase.id == funcionario_id)

    if funcionario is None:
        raise HTTPException(status_code=404, detail="Funcionárion não encontrado")

    return funcionario

@funcionario_router.post(path="/", response_model=FuncionarioReadOne)
def criar_um_funcionario(novo_funcionario: FuncionarioCreate):
    """Cria um funcionario"""

    funcionario = FuncionarioDataBase.create(
        nome=novo_funcionario.nome,
        email=novo_funcionario.email,
        cargo=novo_funcionario.cargo,
    )

    return funcionario

@funcionario_router.put(path="/{funcionario_id}", response_model=FuncionarioReadOne)
def atualizar_um_funcionario(funcionario_id: int, funcionario_atualizado: FuncionarioUpdate):
    """Atualiza um funcionario"""

    funcionario = FuncionarioDataBase.get_or_none(FuncionarioDataBase.id == funcionario_id)

    if funcionario is None:
        raise HTTPException(status_code=404, detail="Funcionárion não encontrado")

    funcionario.cargo = funcionario_atualizado.cargo
    funcionario.email = funcionario_atualizado.email

    funcionario.save()

    return funcionario

@funcionario_router.delete(path="/{funcionario_id}", response_model=FuncionarioReadOne)
def excluir_um_funcionario(funcionario_id: int):
    """Exclui um funcionario"""

    funcionario = FuncionarioDataBase.get(FuncionarioDataBase.id == funcionario_id)

    if funcionario is None:
        raise HTTPException(status_code=404, detail="Funcionárion não encontrado")

    funcionario.delete_instance()

    return funcionario

