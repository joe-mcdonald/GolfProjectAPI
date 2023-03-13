from flask import Flask, render_template
import json
from jinja2 import Template
import time
from bs4 import BeautifulSoup
import requests
# import uploadData

app = Flask(__name__)

soup = BeautifulSoup(requests.get('https://www.espn.com/golf/leaderboard/_/tour/pga').text, "html.parser")
tournament_status = str(soup.find_all("div", class_="status cf mt4 mb4")[0].text)

@app.route("/")
def index():
    if tournament_status == "Final":
        with open("sample.json") as f:
            data = json.load(f)
        return render_template("tournamentNotInSession.html", data=data)
    else:
        with open("sample.json") as f:
            data = json.load(f)
        return render_template("tournamentInSession.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)