from contextlib import asynccontextmanager
from sqlmodel import SQLModel, create_engine

# Configuro la BD SQLite (se crea en db/heroes.db)
sqlite_url = "sqlite:///db/heroes.db"
engine = create_engine(sqlite_url, echo=True)  # echo=True para ver las consultas

# Esto crea las tablas al iniciar la app
@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield