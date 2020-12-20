import requests

def Check(msg: str)-> bool:
    msg = msg.lower().strip()
    return True if (msg!="hi" and msg!="hello" and msg!="help" and msg!="about" and msg!="pigro" and msg!="pigrobot") else False


def Searcher(msg: str)-> str:
    payload = {'skip_disambig':'1', 'format': 'json', 'pretty': '1', 'q': msg}
    req = requests.get('https://api.duckduckgo.com/', params=payload).json()
    ab_text = req['AbstractText']
    if ab_text == "":
        ab_text = req['RelatedTopics'][0]['Text']     
    res = '*'+req["Heading"]+'*'+'\n\n'+ab_text
    return res   
