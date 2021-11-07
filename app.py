from flask import Flask, render_template, redirect
from pymongo import MongoClient
import pymongo
import scraping

app= Flask(__name__)

# Use pymongo to set up mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
mars_info = client.mars_db.mars_info

@app.route("/")
def home():
    marsData= mars_info.find_one()
    return render_template("index.html", marsData= marsData)


@app.route("/scrape")
def scrape():
    MarsInfo = scraping.scrape()
    
    pymongo.db.collection.update({}, MarsInfo, upsert=True)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)