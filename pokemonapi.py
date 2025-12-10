import requests
import csv
import os

BASE_URL = "https://pokeapi.co/api/v2/"

def get_pokemon_data(name):
    url = f"{BASE_URL}pokemon/{name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Couldn't find that Pokémon or network error.")
        return None

def write_csvs_for_pokemon(data, prefix="ditto"):
    # per-stat CSV
    stats = data.get('stats', [])
    stats_file = f"{prefix}_stats.csv"
    with open(stats_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['stat_name', 'base_stat', 'effort']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in stats:
            writer.writerow({
                'stat_name': item['stat']['name'],
                'base_stat': item.get('base_stat'),
                'effort': item.get('effort')
            })
    print(f"Wrote {stats_file}")
    try:
        os.startfile(os.path.abspath(stats_file))
    except OSError:
        print(f"Couldn't open {stats_file} automatically.")

    # summary CSV
    summary = {
        'id': data.get('id'),
        'name': data.get('name'),
        'height': data.get('height'),
        'weight': data.get('weight'),
        'types': ','.join([t['type']['name'] for t in data.get('types', [])]),
        'abilities': ','.join([a['ability']['name'] for a in data.get('abilities', [])])
    }
    summary_file = f"{prefix}_summary.csv"
    with open(summary_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(summary.keys()))
        writer.writeheader()
        writer.writerow(summary)
    print(f"Wrote {summary_file}")
    try:
        os.startfile(os.path.abspath(summary_file))
    except OSError:
        print(f"Couldn't open {summary_file} automatically.")

if __name__ == "__main__":
    # change the name below or replace with input(...) to fetch other Pokémon
    pokemon_name = "ditto"
    data = get_pokemon_data(pokemon_name)
    if data:
        write_csvs_for_pokemon(data, prefix=pokemon_name.lower())
    else:
        print("No data to write.")