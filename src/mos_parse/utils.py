def edit_text(sentence: str) -> str:
    return (
        sentence.replace("\n", "").replace("\t", "").replace("  ", "").replace("\r", "")
    )


def get_new_id(url: str) -> str:
    news_id = url.split("/")[-1]
    news_id = news_id.split("-")[0]

    return news_id


def divide_to_batches(data: list, count):
    batches = []
    for n in range(0, len(data), count):
        batches.append(data[n : n + count])

    return batches