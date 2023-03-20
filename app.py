from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        text = function()
        bold_text = f"<b>{text}</b>"
        return bold_text
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        text = function()
        emphasized_text = f"<em>{text}</em>"
        return emphasized_text
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        text = function()
        underlined_text = f"<u>{text}</u>"
        return underlined_text
    return wrapper_function

@app.route('/')
@make_bold
@make_emphasis
@make_underline
def hello_world():
    return "hello, world!"


@app.route('/user/<username>/<int:number>')
def greet_user(username, number):
    return f"hello {username}. You are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
