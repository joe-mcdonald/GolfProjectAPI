from flask import Flask, render_template
import json
from jinja2 import Template
import time
import uploadData

app = Flask(__name__)

@app.route("/")
def index():
    with open("sample.json") as f:
        data = json.load(f)
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)