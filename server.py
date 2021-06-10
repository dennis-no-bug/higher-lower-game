from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0, 9)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://i.giphy.com/3o7aCSPqXE5C6T8tBC.gif'>"

@app.route("/<int:guess>")
def number_guessing(guess):
    if guess > random_number:
        return "<h1 style='color: red'>Oops, too high! Try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    elif guess < random_number:
        return "<h1 style='color: red'>Oops, too low! Try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    else:
        return "<h1 style='color: green'>Bingo! It's correct!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)


