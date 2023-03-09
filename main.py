import requests

token = '2dd28a0578de0214104570a14d24b21c'

add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons', headers={'Content-Type': 'application/json',
                                                                                        "trainer_token": token},
                                     json={"name": "julija",
                                           "photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print(add_pokemon_response.text)

pokemon_id = add_pokemon_response.json().get('id')

rename_pokemon_response = requests.put('https://pokemonbattle.me:9104/pokemons', headers={'Content-Type': 'application/json',

                                                                                          "trainer_token": token},
                                       json={"pokemon_id": pokemon_id,
                                            "name": "Bond",
                                            "photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print(rename_pokemon_response.text)

add_pokeball_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers={'Content-Type': 'application/json',

                                                                                          "trainer_token": token},
                                       json={"pokemon_id": pokemon_id,
                                            "name": "Bond",
                                            "photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print(add_pokeball_response.text)