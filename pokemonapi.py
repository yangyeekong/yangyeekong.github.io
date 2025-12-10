import requests # Helps us make web requests
 # Base URL of the PokéAPI
 
BASE_URL = "https://pokeapi.co/api/v2/"
 # Function to get data about a specific Pokémon
def get_pokemon_data(name):
    url = f"{BASE_URL}pokemon/{name.lower()}" # Combine base URL and Pokémon name
    try:
        response = requests.get(url) # Make the GET request
        response.raise_for_status()
 # Raise error if status isn't OK (e.g., 404)
        return response.json()
 # Convert the response to JSON
    except:
        print("Couldn't find that Pokémon!")
        return None
 # Test it with a Pokémon name
data = get_pokemon_data("ditto")
 
if data:
     print(data['stats'])