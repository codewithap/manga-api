from requests import get
from bs4 import BeautifulSoup as bs
import json

base_url = "https://myanimelist.net/manga.php?q="


class myanimelist:
    def __init__(self):
        pass

    def search(query):
        r = get(base_url+ query)
        soup = bs(r.text,"html.parser")
        list = soup.select(".list table tr")
        data = '{"data": ['
        # list.pop(0)
        for item in list:
            print(item,"\n\n")
        #     link = item.find("a")["href"]
        #     img = item.find("img")["src"]
        #     title = item.findAll("a")[1].text
        #     info = "{" + f'"img" :"{img}", "title": "{title}", "link": "{link}"'+ "},"
        #     data = data + info
        # jsonData = data[:-1] + ']}'
        return list#json.loads(jsonData)


(myanimelist.search("naruto"))