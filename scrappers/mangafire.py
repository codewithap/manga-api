from requests import get
from bs4 import BeautifulSoup as bs
import json

base_url = "https://mangafire.to/filter?keyword="



class mangafire:
    def __init__(self,query,base_url,):
        super().__init__(query,base_url)
        self.url = base_url
        self.query = query


    def search(self):
        r = get(self.url+ self.query)
        soup = bs(r.text,"html.parser")
        list = soup.select(".mangas .item")
        data = '{"data": ['
        for item in list:
            link = item.find("a")["href"]
            img = item.find("img")["src"]
            title = item.findAll("a")[1].text
            info = "{" + f'"img" :"{img}", "title": "{title}", "link": "{link}"'+ "},"
            data = data + info
        jsonData = data[:-1] + ']}'
        return json.loads(jsonData)
    
    def getChapters(self):
        r = get(self+ self)
        soup = bs(r.text,"html.parser")
        list = soup.select(".mangas .item")
        data = '{"data": ['
        return self


if __name__ == "__main__":
    print(mangafire.getChapters("bleach"))