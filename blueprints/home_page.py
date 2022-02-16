from flask import Blueprint

home_page = Blueprint("home=", __name__)

@home_page.route("/")
def homepage():
    return "Welcome to the home page. To see the directory type /directory into the end of the url"