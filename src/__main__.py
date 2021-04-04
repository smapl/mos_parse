from mos_parse.parse_news import parse
from mos_parse.parse_links import links


if __name__ == "__main__":

    active_links = links()
    for link in active_links:
        parse(link)