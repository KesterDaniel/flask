from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello, world!"


@app.route('/user/<username>/<int:number>')
def greet_user(username, number):
    return f"hello {username}. You are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
