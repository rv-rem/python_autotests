import requests
import pytest

def test_status_code():
    status_code = requests.get('https://pokemonbattle.me:5000/trainers')
    assert status_code.status_code == 200

def test_trainers_name():
    trainers_name = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id' : '1828'})
    assert trainers_name.json()['trainer_name'] == 'rv-rem'