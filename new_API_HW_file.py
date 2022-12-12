import requests
import json
from pprint import pprint
def test_request():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    new_hero = response.json()
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    hero_dict = {}
    for key in new_hero:
        name_hero = key['name']
        if name_hero in hero_list:
            intellig = key.get('powerstats')
            hero_dict.setdefault(name_hero,[intellig['intelligence']])
    print(max(hero_dict.items()))


if __name__ == '__main__':
    test_request()




