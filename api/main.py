from flask import Flask, render_template, request
from scrappers.manganelo import manganelo
from scrappers.myanimelist import myanimelist
from scrappers.mangafire import mangafire
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.route("/")
def home():
  return "🥳🥳🥳🎉🎉🎉🎉🎉"

## myanimelist search ##
@app.route("/api/v1/search/<string:q>")
def search(q):
  data = manganelo.search(q)
  return data

## manganelo search ##
@app.route("/api/v1/manganelo/search/<q>")
def mangaFireSearch(q):
  data = mangafire.search(q)
  return data

## myanimelist manga info ##
@app.route("/api/v1/manga/<id>")
def anime(id):
  data = myanimelist.manga(id)
  return data

## get chapters from manganelo ##
@app.route("/api/v1/manganelo/chapters/<name>")
def chapters(name): 
  chapData = manganelo.getChapters(id)
  return chapData

## list of top animes from myanimelist ##
@app.route("/api/v1/top")
def topAnime(): 
  page = request.args.get("page")
  data = myanimelist.topMangas(page)
  return data
  
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True)
