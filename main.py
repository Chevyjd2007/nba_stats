import requests
from datetime import datetime
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
    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        date_str = data['parameters']['date']
        date = datetime.strptime(date_str, "%Y-%m-%d")
        formatted_date = date.strftime("%B %d, %Y")
        print(f"NBA games on {formatted_date}:")

        for game in data['response']:
            home = game['teams']['home']['code']
            away = game['teams']['visitors']['code']
            score_home = game['scores']['home']['points']
            score_away = game['scores']['visitors']['points']
            quarter = game['periods']['current']
            clock = game['status']['clock']
            home_nick = game['teams']['home']['nickname']
            away_nick = game['teams']['visitors']['nickname']

            print(f"{home} vs {away}")
            if quarter == 4 and clock is not None:
                print(f"{quarter}: {score_home} - {score_away}")
            elif score_home > score_away:
                print(f"Final: {score_home} - {score_away} --------> {home_nick} Win!")
            else:
                print(f"Final: {score_home} - {score_away} --------> {away_nick} Win!")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


user_date = input("Welcome! Please specify a date (year-month-day): ")
params = {"date": user_date}
get_games(params)