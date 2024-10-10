from http.client import HTTPException

from fastapi import APIRouter

from app.models import CategoriaDataBase
from app.schemas import CategoriareadOne, CategoriaReadAll, CategoriaCreate, CategoriaUpdate

categoria_routers = APIRouter(prefix="/categorias", tags=["Categoria"])

@categoria_routers.get(path="/", response_model=CategoriaReadAll)
def listar_todas_as_categoria():
    """Lista todas as categorias"""

    categorias = CategoriaDataBase.select()

    return {"categorias": categorias}

@categoria_routers.get(path="/{categoria_id}", response_model=CategoriareadOne)
def lista_uma_categoria(categoria_id):
    """Lista uma categoria"""

    categoria = CategoriaDataBase.get_or_none(CategoriaDataBase.id == categoria_id)

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    else:
        return categoria

@categoria_routers.post(path="/", response_model=CategoriareadOne)
def criar_categoria(nova_categoria: CategoriaCreate):
    """Cria uma nova categoria"""

    categoria = CategoriaDataBase.create(
        nome=nova_categoria.nome,
    )

    return categoria

@categoria_routers.put(path='/{categoria_id}', response_model=CategoriareadOne)
def atualizar_categoria(categoria_id: int, categoria_atualizada: CategoriaUpdate):
    """Atualiza uma categoria"""

    categoria = CategoriaDataBase.get_or_none(CategoriaDataBase.id == categoria_id)

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    categoria.nome = categoria_atualizada.nome
    categoria.save()

    return categoria

@categoria_routers.delete(path='/categoria/{categoria_id}', response_model=CategoriareadOne)
def deletar_categoria(categoria_id: int):
    """Deleta uma categoria"""

    categoria = CategoriaDataBase.get_or_none(CategoriaDataBase.id == categoria_id)

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    categoria.delete_instance()

    return categoria
