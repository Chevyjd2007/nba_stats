import requests
from requests import get
from pprint import PrettyPrinter

URL = "https://free-nba.p.rapidapi.com/stats"
querystring = {"seasons":"2022","page":"0","per_page":"25","player_ids":"237","dates":"2023-05-06"}

headers = {
    "X-RapidAPI-Key": "47a3be4347msh11b56a9873dc9b6p11e463jsndbba2a2cdd00",
    "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

printer = PrettyPrinter()
response = requests.get(URL, headers=headers, params=querystring)

printer.pprint(response.json())

