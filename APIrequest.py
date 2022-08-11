import requests
import json
class API:
    def __init__(self):
        pass
    def request(self, i, parse_data):
        response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
        if response.status_code == 200:
            id = parse_data[i-1]['id']
            name = parse_data[i-1]['name']
            aliases = parse_data[i-1]['biography']['aliases'][0]
            int = parse_data[i-1]['powerstats']['intelligence']
            strength = parse_data[i-1]['powerstats']['strength']
            speed = parse_data[i-1]['powerstats']['speed']
            durability = parse_data[i-1]['powerstats']['durability']
            power = parse_data[i-1]['powerstats']['power']
            combat = parse_data[i-1]['powerstats']['combat']
            image = parse_data[i-1]['images']['md']
            if id == None:
                id = "NULL"
            if name == None:
                name = "NULL"
            if aliases == None:
                aliases = "NULL"
            if int == None:
                int= "NULL"
            if strength == None:
                strength = "NULL"
            if speed == None:
                speed = "NULL"
            if durability == None:
                durability = "NULL"
            if power == None:
                power = "NULL"
            if combat == None:
                combat = "NULL"
            if image == None:
                image = "NULL"
            return [id, name, aliases, int, strength, speed, durability, power, combat, image]
        else:
            return False