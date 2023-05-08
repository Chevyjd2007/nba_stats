from requests import get
from pprint import PrettyPrinter

Base_URL = "https://data.nba.net/"
ALL_JSON = "/prod/v1/today.json"
printer = PrettyPrinter()


def get_links():
    data = get(Base_URL + ALL_JSON).json()
    links = data["links"]
    return links


def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(Base_URL + scoreboard).json()['games']
    date = get_links()['currentDate']

    print(f"NBA games on {date[4:6]} - {date[6:]} - {date[:4]}:")

    for game in games:
        home = game["hTeam"]
        away = game["vTeam"]
        clock = game["clock"]
        period = game['period']

        print(f"{home['triCode']} vs {away['triCode']}")
        print(f"{home['score']} - {away['score']}")
        print(f"Clock: {clock} || Quarter: {period['current']}")
        print("___________________________________________")

def get_stats():
    stats = get_links()['leagueConfStandings']
    standing = get(Base_URL + stats).json()

    printer.pprint(standing)


get_scoreboard()
#  get_stats()
