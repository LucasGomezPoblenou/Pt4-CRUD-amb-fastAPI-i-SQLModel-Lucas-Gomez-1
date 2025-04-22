from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from models import Hero, HeroCreate, HeroPublic, Team, TeamCreate, TeamPublic
from database import engine, lifespan

# creo l'app amb la base de dades que vam fer
app = FastAPI(lifespan=lifespan)

# ruta del principi per probar si va la api
@app.get("/")
def read_root():
    return {"message": "API de Héroes y Equipos"}

# aquí va lo de crear equips i llegir-los

# afegeixo un equip nou
@app.post("/teams/", response_model=TeamPublic)
def create_team(team: TeamCreate):
    with Session(engine) as session:
        db_team = Team.from_orm(team)
        session.add(db_team)
        session.commit()
        session.refresh(db_team)
        return db_team

# veure tots els equips que hi ha
@app.get("/teams/", response_model=list[TeamPublic])
def read_teams():
    with Session(engine) as session:
        teams = session.exec(select(Team)).all()
        return teams

# aqui llegeixo un equip sol (vull veure també els herois que té si pot ser)
@app.get("/teams/{team_id}", response_model=TeamPublic)
def read_team(team_id: int):
    with Session(engine) as session:
        team = session.get(Team, team_id)
        if not team:
            raise HTTPException(status_code=404, detail="Equipo no encontrado")
        return team

# modificar un equip (no sabia si fer put o patch, he posat patch q es mes lleuger)
@app.patch("/teams/{team_id}", response_model=TeamPublic)
def update_team(team_id: int, team: TeamCreate):
    with Session(engine) as session:
        db_team = session.get(Team, team_id)
        if not db_team:
            raise HTTPException(status_code=404, detail="Equipo no encontrado")
        team_data = team.dict(exclude_unset=True)
        for key, value in team_data.items():
            setattr(db_team, key, value)
        session.add(db_team)
        session.commit()
        session.refresh(db_team)
        return db_team
