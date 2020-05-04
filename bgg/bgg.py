#!/usr/bin/python

from boardgamegeek import BGGClient
from PIL import Image
import requests
from io import BytesIO

USER = "andypiper"


def show_image(url):
    """Display an image from the web on the iOS Python terminal"""
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


bgg = BGGClient()
user_collection = bgg.collection(USER, exclude_subtype = "boardgameexpansion", own = True)

number_of_games = len(user_collection.items)
print(f"{USER} has {number_of_games} games in their collection\n\n")

for i in range(number_of_games):
    game = user_collection.items[i]
    show_image(url = game.thumbnail)  # image is nicer, but slow to fetch
    data = (
		f"{game.name} \n" 
		f"Players {game.min_players} - {game.max_players} \n"
		f"Time {game.min_playing_time} - {game.max_playing_time} \n")
    print(data)
    