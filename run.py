from flask import Flask
from blueprints.car_models import car_parts
from blueprints.computer_models import computer_details
from blueprints.home_page import home_page
from blueprints.test_dict_page import direct_page

app = Flask(__name__)

app.register_blueprint(car_parts, url_prefix="/car")
app.register_blueprint(computer_details, url_prefix="/computer")
app.register_blueprint(home_page, url_prefix="/")
app.register_blueprint(direct_page, url_prefix="/directory")