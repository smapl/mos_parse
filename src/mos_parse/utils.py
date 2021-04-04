def edit_text(sentence: str) -> str:
    return (
        sentence.replace("\n", "").replace("\t", "").replace("  ", "").replace("\r", "")
    )


def get_new_id(url: str) -> str:
    new_id = url.split("/")[-1]
    new_id = new_id.split("-")[0]

    return new_id
