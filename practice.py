# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authenticated(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
# @is_authenticated
# def create_blog(user):
#     print(f"{user.name} has a new post")
#
# new_user = User("kester")
# new_user.is_logged_in = True
# create_blog(new_user)
import random





# CHALLENGE
from flask import Flask
app = Flask(__name__)

magic_number = random.randint(0, 9)

@app.route("/")
def home():
    return "Home page"

@app.route("/<int:guess>")
def make_guess(guess):
    if guess > magic_number:
        return "<h1>Too high</h1>"
    elif guess < magic_number:
        return "<h1>Too low</h1>"
    else:
        return "You gat it"


if __name__ == "__main__":
    app.run(debug=True)