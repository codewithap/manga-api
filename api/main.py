from flask import Flask, render_template, request
from scrappers.manganelo import manganelo
from scrappers.myanimelist import myanimelist
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.route("/")
def home():
  
  return ""

@app.route("/api/v1/search")
def search():
  query = request.args.get("q")
  data = myanimelist.search(query)
  return data
  
  
@app.route("/api/v1/manga")
def getmanga():
  chapters = request.args.get("id")
  return ""

@app.route("/api/v1/top")
def topManga():
  page = request.args.get("page")
  data = myanimelist.topMangas(page)
  return data
  
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True)
