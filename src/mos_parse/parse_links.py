import requests

from bs4 import BeautifulSoup
from pymongo import MongoClient
from loguru import logger
from tqdm import tqdm

from .dates import DATES


client = MongoClient()
db = client["echo_of_moscow"]
collection = db["error_log_links"]


def links() -> list:
    links = []
    logger.info("Starting generating")
    for month in DATES:
        for day in tqdm(DATES[month]):
            url = f"https://echo.msk.ru/news/own/2020/{month}/{day}/"

            try:
                resp = requests.get(url)
                soup = BeautifulSoup(resp.text, "html5lib")
                all_links = soup.find("div", {"class", "column"})
                page_link = all_links.find_all("h3")

                for link in page_link:
                    url = link.find("a").get("href")
                    links.append(f"https://echo.msk.ru{url}")

            except Exception as ex:
                collection.insert_one({"url": url})
                logger.error(ex)
                continue

    return links
