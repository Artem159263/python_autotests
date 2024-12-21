import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '328bd710526b6581e9b2fb1a27c57637'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token': TOKEN }
TRAINER_ID = 12740
def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : 12740})
    assert response.status_code == 200