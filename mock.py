from sqlmodel import Session, SQLModel, create_engine
from models import Hero, Team

engine = create_engine("sqlite:///db/heroes.db")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_heroes_and_teams():
    with Session(engine) as session:
        # Creo 2 equipos
        team_avengers = Team(name="Avengers", headquarters="Nueva York")
        team_xmen = Team(name="X-Men", headquarters="Mansión X")
        session.add(team_avengers)
        session.add(team_xmen)
        session.commit()

        # Creo héroes y los asigno a equipos
        heroes = [
            Hero(name="Iron Man", secret_name="Tony Stark", age=45, team_id=team_avengers.id),
            Hero(name="Spider-Man", secret_name="Peter Parker", age=16, team_id=team_avengers.id),
            Hero(name="Wolverine", secret_name="Logan", age=100, team_id=team_xmen.id),
        ]
        for hero in heroes:
            session.add(hero)
        session.commit()

if __name__ == "__main__":
    create_db_and_tables()
    create_heroes_and_teams()
    print("¡BD creada con equipos y héroes!")