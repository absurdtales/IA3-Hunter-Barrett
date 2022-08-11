import requests
import json
# connect to API
response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
# if response code allows it then load json data as text and print
if response.status_code == 200:
    data = response.text
    parse_data = json.loads(data)
    print(parse_data)
# or print an error
else:
    print("Error loading API")