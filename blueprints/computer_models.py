from flask import Blueprint

computer_details = Blueprint("computer_parts=", __name__)

@computer_details.route("/")
def computer():
    return """This is a string on multiple lines testing if flask will
    return a string that is formatted in multiple lines in this way.
    I like computer parts.
    I have a 2080 ti super graphics card.
    I have an intel i9 CPU.
    I have 24gbs of RAM."""