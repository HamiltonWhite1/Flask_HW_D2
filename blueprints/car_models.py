from flask import Blueprint

car_parts = Blueprint("name=", __name__)

@car_parts.route("/")
def car():
    return "This is a car"

@car_parts.route("/tires")
def tires():
    return "These are the car's tires"

@car_parts.route("/engine")
def engine():
    return "This is the car's engine"

@car_parts.route("/color")
def color():
    return "The car is blue"

@car_parts.route("/make")
def make():
    return "This car is a Toyota"

@car_parts.route("/year")
def year():
    return "This car was made in 2004"

@car_parts.route("/model")
def model():
    return "This car is a 4runner"