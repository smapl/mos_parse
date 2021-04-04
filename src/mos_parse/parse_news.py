import requests

from bs4 import BeautifulSoup
from loguru import logger

from .utils import edit_text, get_new_id
from .header import HEADER


def get_comms(id_news: str) -> str:

    resp = requests.get(f"https://echo.msk.ru/elements/{id_news}/comments_scroll.html")
    soup = BeautifulSoup(resp.text, "html5lib")

    comments = soup.find("div", {"class": "commBlock"}).text
    comments = edit_text(comments)

    logger.info(comments)

    return comments


def parse(url: str):
    news = {}

    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.text, "html5lib")

    news["title"] = soup.find("h1").text

    core_new = soup.find("div", {"class": "typical"}).text
    news["core_new"] = edit_text(core_new)

    new_id = get_new_id(url)
    news["comments"] = get_comms(new_id)

    logger.info(news)
