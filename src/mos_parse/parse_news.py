import requests
import json

from bs4 import BeautifulSoup
from loguru import logger
from pymongo import MongoClient

from .utils import edit_text, get_new_id
from .header import HEADER

client = MongoClient()
db = client["echo_of_moscow"]
collection = db["news"]


def get_comms(id_news: str) -> tuple:

    resp = requests.get(f"https://echo.msk.ru/elements/{id_news}/comments_scroll.html")
    soup = BeautifulSoup(resp.text, "html5lib")

    comments = soup.find_all("div", {"class": "commBlock"})
    if len(comments) == 0:
        return (False, None)

    dict_comments = {}
    for comment in comments:

        try:
            author = comment.find("strong", {"class": "name"}).text
            author = edit_text(author)
        except:
            author = "None"

        try:
            data = comment.find("p", {"class": "commtext"}).text
            data = edit_text(data)
        except:
            data = "None"

        dict_comments[author] = data

    return (True, dict_comments)


def parse(url: str):
    news = {}
    news["url"] = url
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.text, "html5lib")

    news["title"] = soup.find("h1").text

    core_new = soup.find("div", {"class": "typical"}).text
    news["core_new"] = edit_text(core_new)

    new_id = get_new_id(url)
    comments = get_comms(new_id)

    if comments[0]:
        news["comments"] = comments[1]

    else:
        news["comments"] = "empty"

    try:
        collection.insert_one(news)

    except Exception as ex:
        logger.error(ex)
