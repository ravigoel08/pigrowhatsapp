import requests

# perform some checks on message recieved from user end
def Check(msg: str)-> bool:
    msg = msg.lower().strip()
    return (
        False if msg in ["hi", "hello", "help", "about", "pigro", "pigrobot"] else True
    )


# search wikipedia for information and return a formated string
def Searcher(msg: str)-> str:
    payload = {'skip_disambig':'1', 'format': 'json', 'pretty': '1', 'q': msg}
    req = requests.get('https://api.duckduckgo.com/', params=payload).json()
    ab_text = req['AbstractText']
    if ab_text == "":
        ab_text = req['RelatedTopics'][0]['Text']     
    res = '*'+req["Heading"]+'*'+'\n\n'+ab_text
    return res   
