import requests
from requests import get
from pprint import PrettyPrinter

URL = "https://api-nba-v1.p.rapidapi.com/games"
headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}


printer = PrettyPrinter()
# printer.pprint(response.json())


def get_games(params):
    response = requests.get(URL, headers=headers, params=params)
    date = response.json()['parameters']
    date = date['date']
    print(f"NBA games on {date[-5:-3]} - {date[-2:]} - {date[:4]}:")

    for game in response.json()['response']:
        home = game['teams']['home']['code']
        away = game['teams']['visitors']['code']
        score_home = game['scores']['home']['points']
        score_away = game['scores']['visitors']['points']
        quarter = game['periods']['current']
        clock = game['status']['clock']
        home_nick = game['teams']['home']['nickname']
        away_nick = game['teams']['visitors']['nickname']

        print(home + " vs " + away)
        if quarter == 4 and clock is not None:
           print(str(quarter) + ": " + str(score_home) + " - " + str(score_away))
        elif score_home > score_away:
            print("Final: " + str(score_home) + " - " + str(score_away) + " --------> " + home_nick + " Win!")
        else:
            print("Final: " + str(score_home) + " - " + str(score_away) + " --------> " + away_nick + " Win!")


user_date = input("Welcome! Please specify a date(year-month-day): ")
params = {"date": user_date}

get_games(params)
