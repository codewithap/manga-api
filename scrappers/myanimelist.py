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
      list.pop(0)
      for item in list:
        link = item.find("a")["href"]
        img = item.find("img")["data-srcset"].split(",")
        type = item.findAll("td")[2].text.replace("\n","").strip(" ")
        img1 = img[0].split()[0]
        img2 = img[1].split()[0]
        title = (item.findAll("a")[1].text)
        while True:
          if title.find('"') == -1:
            break
          title = title.replace('"',"")
        data = data +  "{"+f'"type": "{type}","title": "{title}", "link": "{link}", "img" : ["{img1}","{img2}"]'+"},"
      jsonData = data[0:-1] + ']}'
      return json.loads(jsonData)



if __name__ == "__main__":
  print(myanimelist.search("naruto"))
