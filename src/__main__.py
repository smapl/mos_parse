from multiprocessing import Pool

from tqdm import tqdm
from loguru import logger

from mos_parse.parse_news import parse
from mos_parse.parse_links import links
from mos_parse.utils import divide_to_batches


if __name__ == "__main__":

    active_links = links()
    batches = divide_to_batches(active_links, 100)
    logger.info("Starting parse news")

    with Pool(3) as pool:
        max_ = len(batches)
        with tqdm(total=max_) as pbar:
            for i, _ in enumerate(pool.imap_unordered(parse, batches)):
                pbar.update()