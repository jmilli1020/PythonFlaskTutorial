from flask import Flask
from datetime import datetime
from flask import render_template
import re

app = Flask(__name__)

#UI Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

#Tests routes
@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route("/hello-template/")
@app.route("/hello-template/<name>")
def hello_there_template(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
    
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")