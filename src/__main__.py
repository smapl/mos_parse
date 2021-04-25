from tqdm import tqdm
from loguru import logger

from mos_parse.parse_news import parse
from mos_parse.parse_links import links


if __name__ == "__main__":

    active_links = links()
    logger.info("Starting parse news")
    for link in tqdm(active_links):
        parse(link)