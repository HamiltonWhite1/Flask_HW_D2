from flask import Blueprint

direct_page = Blueprint("dict=", __name__)

@direct_page.route("/")
def direct_page_func():
    test_dict_display = {
        "Car": {
            "Home": '/car',
            "Engine": '/car/engine',
            "Tires": '/car/tires',
            "Color": '/car/color',
            "Make": '/car/make',
            "Year": '/car/year',
            "Model": '/car/model'
        },
        "Computer": '/computer'
    }
    return test_dict_display