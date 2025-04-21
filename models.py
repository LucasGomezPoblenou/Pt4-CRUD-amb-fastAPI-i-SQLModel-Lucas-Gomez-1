from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

# Primero defino el modelo Team (Equipo)
class TeamBase(SQLModel):
    name: str = Field(index=True)        # Nombre del equipo (obligatorio)
    headquarters: str                    # Sede del equipo (ej: "Nueva York")

# Esto ya es la tabla en la BD
class Team(TeamBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # ID automático
    heroes: List["Hero"] = Relationship(back_populates="team")  # Relación 1-N (un equipo tiene muchos héroes)

# Ahora el modelo Hero (igual que antes pero con team_id)
class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")  # Clave foránea (link al equipo)
    team: Optional[Team] = Relationship(back_populates="heroes")         # Relación inversa

# Estos son para recibir datos al crear/actualizar
class TeamCreate(TeamBase):
    pass

class HeroCreate(HeroBase):
    team_id: Optional[int] = None  # Aquí sí permito team_id opcional

class TeamPublic(TeamBase):
    id: int

class HeroPublic(HeroBase):
    id: int
    team_id: Optional[int] = None