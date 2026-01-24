import requests
import pandas as pd
import time

url = "https://pokeapi.co/api/v2/pokemon?limit=20"
todos_los_pokemon = []

while url:
    # 1. Realizar la petición
    res = requests.get(url)
    # 2. Extraer los datos en formato JSON
    data = res.json()
    # 3. Añadir los resultados a la lista global
    todos_los_pokemon.extend(data['results'])

    # 4. Crucial: Actualizar la url con la clave 'next'
    # Cuando no haya más páginas, data['next'] será None y el bucle terminará
    url = data['next']

    # 5. Pausa de cortesía para no saturar la API
    time.sleep(0.5)

    print(f"Obtenidos {len(todos_los_pokemon)} Pokémon...")

print("Hemos almacenado todos los pokemons vamos a sacar su información")


lista_pokemons = []

for i,pokemon in enumerate(todos_los_pokemon):

    indice = i + 1

    # Realizar las peticiones con las url de cada pokemon
    url_pokemon = requests.get(pokemon['url'])
    #  Extraer los datos en formato JSON
    json_pokemon = url_pokemon.json()

    # Sacamos la información de cada pokemon
    pokemon_name = json_pokemon['name']
    pokemon_height = json_pokemon['height']
    pokemon_weight = json_pokemon['weight']
    pokemon_base_experience = json_pokemon['base_experience']
    Altura_m =  pokemon_height / 10
    Peso_kg = pokemon_weight / 10

    Pokemons = {  "indice" : indice,
                "Nombre" : pokemon_name,
                "Altura" : pokemon_height,
                "Peso" : pokemon_weight,
                "Base_Experience" : pokemon_base_experience,
                "Altura_m" : Altura_m,
                "Peso_kg" : Peso_kg,
                "BMI": round(Peso_kg / (Altura_m ** 2), 2)
                }
    print(Pokemons)
    lista_pokemons.append(Pokemons)

print("¡Extracción finalizada!")

# Convertir a DataFrame y guardar
df = pd.DataFrame(lista_pokemons)
df.to_csv('pokemitas.csv', index=False)















