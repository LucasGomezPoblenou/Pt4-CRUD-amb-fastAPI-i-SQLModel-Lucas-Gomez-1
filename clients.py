import requests

# aqui poso la base de la api
BASE = "http://127.0.0.1:8000"

# primer provo de crear un equip
print("Creo un equip...")
r = requests.post(BASE + "/teams/", json={"name": "Guardians", "headquarters": "Espai"})
print(r.json())

# ara llegeixo tots els equips per veure si surt
print("Equips que tinc:")
r = requests.get(BASE + "/teams/")
print(r.json())

# crear heroi nou
print("Creo un heroi...")
r = requests.post(BASE + "/heroes/", json={"name": "Groot", "secret_name": "Groot", "age": 8, "team_id": 1})
print(r.json())

# mirar tots els herois
print("Tots els herois que hi ha:")
r = requests.get(BASE + "/heroes/")
print(r.json())

# provo d'actualitzar el team
print("Update team...")
r = requests.patch(BASE + "/teams/1", json={"name": "NOU NOM", "headquarters": "Canviat"})
print(r.json())

# llegir un equip sol
print("Equip amb id 1:")
r = requests.get(BASE + "/teams/1")
print(r.json())
