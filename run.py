from flask import Flask
from blueprints.car_models import car_parts

app = Flask(__name__)

app.register_blueprint(car_parts, url_prefix="/")
app.register_blueprint(car_parts, url_prefix="/tires")
app.register_blueprint(car_parts, url_prefix="/engine")
app.register_blueprint(car_parts, url_prefix="/color")
app.register_blueprint(car_parts, url_prefix="/make")
app.register_blueprint(car_parts, url_prefix="/model")
app.register_blueprint(car_parts, url_prefix="/year")