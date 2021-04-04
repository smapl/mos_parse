import requests

from bs4 import BeautifulSoup
from loguru import logger

from .utils import edit_text, get_new_id

headers = {
    "authority": "echo.msk.ru",
    "method": "GET",
    "path": "/news/2564349-echo.html",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "_grf_vis=1; _grf_ref=www.google.com; tmr_lvid=5ebd0f03a069645f460a51cac4ad4b7d; tmr_lvidTS=1617560192487; bltsr=1; addruid=s1l6t1h7w5g6y0y1v9f8d6t0f6; cmtchd=MTYxNzU2MDE5ODcyMg==; last_visit=1617551166844::1617561966844; tmr_detect=0%7C1617561969169; tmr_reqNum=54",
    "referer": "https://echo.msk.ru/news/own/2020/01/01/",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
}


def get_comms(id_new: str) -> str:
    logger.info("get comms")
    resp = requests.get("https://echo.msk.ru/elements/2564349/comments_scroll.html")
    soup = BeautifulSoup(resp.text, "html5lib")
    comments = soup.find("div", {"class": "commBlock"}).text
    comments = edit_text(comments)
    logger.info(comments)

    return comments


def parse(url: str):
    news = {}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html5lib")

    news["title"] = soup.find("h1").text

    core_new = soup.find("div", {"class": "typical"}).text
    news["core_new"] = edit_text(core_new)

    new_id = get_new_id(url)
    news["comments"] = get_comms(new_id)

    logger.info(news)
