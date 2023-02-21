from requests import get
from bs4 import BeautifulSoup as bs
import json

base_url = "https://myanimelist.net/manga.php?q="
base_manga_url= "https://myanimelist.net/manga/"


class myanimelist:
    def __init__(self):
        pass

    def search(query):
      not_found = {"error" : "File not found","massage" : f"Your search '{query}' did not match any documents"}
      r = get(base_url+ str(query))
      soup = bs(r.text,"html.parser")
      list = soup.select(".list table tr")
      data = '{"data": ['
      if len(list) == 0:
        return not_found
      else:
        list.pop(0)
        for item in list:
          id = item.find("a")["href"].replace("https://myanimelist.net/manga/","").split("/")[0]
          img = item.find("img")["data-srcset"].split(",")
          type = item.findAll("td")[2].text.replace("\n","").strip(" ")
          img1 = img[0].split()[0]
          img2 = img[1].split()[0]
          title = (item.findAll("a")[1].text)
          while True:
            if title.find('"') == -1:
              break
            title = title.replace('"',"")
          data = data +  "{"+f' "mal_id": {id}, "type": "{type}","title": "{title}", "img" : ["{img1}","{img2}"]'+"},"
        jsonData = data[0:-1] + ']}'
        return json.loads(jsonData)

    def manga(id):
      not_found = {"error" : "File not found","massage" : f"Id  '{id}' did not match any documents"}
      r = get(base_manga_url+ str(id))
      soup = bs(r.text,"html.parser")
      img = soup.select(".status-block .icon-thumb")[0]["data-image"]
      print(img)
      data = '{"data": ['
      if len(list) == 0:
        return not_found

    def topMangas(page):
      r = get(base_manga_url+f"ranking.json?offset={30*(int(page)-1)}")
      return json.loads(r.txt)
      
      
if __name__ == "__main__":
  print(myanimelist.manga(11))

