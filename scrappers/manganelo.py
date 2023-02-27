import requests
from bs4 import BeautifulSoup as bs
import json

class manganelo:
  def __init__(self):
    self.base_url = "https://ww5.manganelo.tv/"

  def search(query): 
    r = requests.get(f"https://m.manganelo.com/search/{query}").text
    soup = bs(r, 'html.parser')
    html = soup.select(".panel-search-story .search-story-item")
    data = '{"data": ['
    for item in html:
      img = "https://ww5.manganelo.tv"+item.find("img")["src"]
      title = item.find("img")["alt"]
      link = item.find("a")["href"].replace("/manga/","")
      info = "{" + f'"img" :"{img}", "title": "{title}", "id": "{link}"'+ "},"
      data = data + info
    jsonData = data[:-1] + ']}'
    return json.loads(jsonData)

  # returns all chapters name and list from mangaLink
  def getChapters(link): 
    r = requests.get(link).text
    soup = bs(r, 'html.parser')
    html = soup.select("a.chapter-name")
    data = '{"data": ['
    for item in html: 
      title = item.text
      link = "https://ww5.manganelo.tv"+item["href"]
      info = "{" + f'"title": "{title}", "link": "{link}"'+ "},"
      data = data+info
    jsonData = data[:-1] + ']}'
    return json.loads(jsonData)

  # returns the list of mangaJpgs
  def getManga(url): 
    r = requests.get(url).text
    soup = bs(r, 'html.parser')
    html = soup.select(".container-chapter-reader img")
    imgs = []
    for item in html:
      imgs.append(item["data-src"])
    return imgs



#print(getManga("https://ww5.manganelo.tv/chapter/manga-gi983965/chapter-6"))

