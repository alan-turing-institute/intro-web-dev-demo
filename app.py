from flask import render_template, request, make_response, Response
from datetime import datetime

import flask

app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess() -> Response:
    user_guess: int = 0
    if str(request.form["guess"]).isdigit():
        user_guess = int(request.form["guess"])

    answer: int = 42
    user_message: str = ""

    if user_guess < answer:
        user_message = "Your guess is too low"
    elif user_guess > answer:
        user_message = "Your guess is too high"
    else:
        user_message = "Congratulations!"

    response_html: str = f"""<pre>
            Your guess is {user_guess}. 
            {user_message}.
            </pre>
            <form method='post' action='/'>
            <p>Enter Guess: <input type='text' name='guess'/></p>
            <p><input type="submit"></p>
            </form>
            """

    response_object: Response = make_response(response_html)
    response_object.headers["Content-Type"] = "text/html"

    return response_object


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template("hello_there.html", name=name, date=datetime.now())


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
