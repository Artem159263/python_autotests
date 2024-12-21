import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '328bd710526b6581e9b2fb1a27c57637'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token': TOKEN }
body_create = {
    "name": "Python",
    "photo_id": 9
}
body_change = {
    "pokemon_id": "164567",
    "name": "Pythonv1",
    "photo_id": 10
}
body_pokeboll = {
    "pokemon_id": "164567"
}

response_create = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/pokemons' , headers = HEADER, json = body_change)
print(response_change.text)

response_change = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER, json = body_pokeboll)
print(response_change.text)

