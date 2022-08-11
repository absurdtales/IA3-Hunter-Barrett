import requests
import json
response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
if response.status_code == 200:
    data = response.text
    parse_data = json.loads(data)
    print(parse_data)
else:
    print("Error loading API")