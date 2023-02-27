from requests import get
from bs4 import BeautifulSoup as bs
import json

base_url = "https://mangafire.to/filter?keyword="



class mangafire:
    def __init__(self):
        pass


    def search(query):
        r = get(base_url+ query)
        soup = bs(r.text,"html.parser")
        list = soup.select(".mangas .item")
        data = '{"data": ['
        for item in list:
            link = item.find("a")["href"].replace("/manga/","")
            img = item.find("img")["src"]
            title = item.findAll("a")[1].text
            info = "{" + f'"img" :"{img}", "title": "{title}", "id": "{link}"'+ "},"
            data = data + info
        jsonData = data[:-1] + ']}'
        return jsonData #json.loads(jsonData)
    
    def getChapters(id):
        r = get("https://mangafire.to/manga/"+id)
        soup = bs(r.text,"html.parser")
        list = soup.find("ul", {"data-name": "EN"}).select("li")
        data = '{"data": ['
        for item in list: 
          link = item.find("a")["href"]
          title = item.find("a")["title"]
          info = "{" + f'"link" :"{link}", "title": "{title}"'+ "},"
          data = data + info
        jsonData = data[:-1] + ']}'
        return json.loads(jsonData)


if __name__ == "__main__":
    print(mangafire.search("one punch man"))
    
