import requests

token = '45f2d377f037f94d5802247dd4b8b349'

pokemons_creat = requests.post('https://pokemonbattle.me:5000/pokemons', json = {
    "name": "4uvak",
    "photo": "https://dolnikov.ru/pokemons/05.png"
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print(pokemons_creat.text)



pokemons_edit = requests.put('https://pokemonbattle.me:5000/pokemons', json = {
    "pokemon_id": 3177,
    "name": "Super4uvak",
    "photo": "https://dolnikov.ru/pokemons/05.png"
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print(pokemons_edit.text)



pokemons_add_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', json = {
    "pokemon_id": "3177"
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print(pokemons_add_pokeball.text)