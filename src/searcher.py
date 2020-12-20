import requests
from typing import str, bool
import constants

def check(msg: str) -> bool:
    msg = msg.lower().strip()
    return (
        False if msg in ["hi", "hello", "help", "about", "pigro", "pigrobot"] else True
    )


def searcher(msg: str) -> str:
    payload = {"skip_disambig": "1", "format": "json", "pretty": "1", "q": msg}
    req = requests.get(constants.URL, params=payload).json()
    ab_text = req["AbstractText"]
    if ab_text == "":
        ab_text = req["RelatedTopics"][0]["Text"]
    res = f'*{req["Heading"]}*\n\n{ab_text}'
    return res
