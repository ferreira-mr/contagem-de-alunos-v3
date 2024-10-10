from pydantic import BaseModel

class FuncionarioCreate(BaseModel):
    nome: str
    email: str
    cargo: str

class FuncionarioReadOne(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str

class FuncionarioReadAll(BaseModel):
    funcionarios: list[FuncionarioReadOne]


class FuncionarioUpdate(BaseModel):
    email: str
    cargo: str


class CategoriaCreate(BaseModel):
    nome: str

class CategoriareadOne(BaseModel):
    id: int
    nome: str

class CategoriaReadAll(BaseModel):
    categorias: list[CategoriareadOne]

class CategoriaUpdate(BaseModel):
    nome: str

class TurmaCreate(BaseModel):
    name: str
    categoria_id: str

class TurmaRead(BaseModel):
    id: int
    nome: str
    categoria: CategoriareadOne

class TurmaReadAll(BaseModel):
    turmas: list[TurmaRead]

class TurmaUpdate(BaseModel):
    nome: str

