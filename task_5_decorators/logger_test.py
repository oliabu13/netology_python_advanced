import requests
from main import decorator


@decorator(path=' ')
def get_id(name):
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    all_superheros = response.json()
    for superhero in all_superheros:
        if name == superhero['name']:
            sup_id = str(superhero['id'])
    return f'ID супергероя: {sup_id}'


get_id('Hulk')



