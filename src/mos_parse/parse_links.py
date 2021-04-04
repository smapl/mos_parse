import requests

from bs4 import BeautifulSoup
from loguru import logger

from .dates import DATES


def links() -> list:
    links = []
    for month in DATES:
        for day in DATES[month]:
            url = f"https://echo.msk.ru/news/own/2020/{month}/{day}/"

            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, "html5lib")
            all_links = soup.find("div", {"class", "column"})
            page_link = all_links.find_all("h3")

            for link in page_link:
                url = link.find("a").get("href")
                links.append(f"https://echo.msk.ru{url}")

    return links
