from flask import request, make_response, Response

import flask
import logging

app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess() -> Response:
    user_guess: int = -1
    try:
        form_data: str = request.get_data(as_text=True)
        user_guess = int(form_data.split("=")[1])
    except:
        logging.warn("We couldn't get a user answer")

    answer: int = 42
    user_message: str = ""

    if 0 < user_guess < answer:
        user_message = f"Your guess is {user_guess}. Your guess is too low."
    elif user_guess > answer:
        user_message = f"Your guess is {user_guess}. Your guess is too high."
    elif user_guess == answer:
        user_message = f"Your guess is {user_guess}. Congratulations!"

    response_html: str = f"""<pre>
            {user_message}
            </pre>
            <form method='post' action='/'>
            <p>Enter Guess: <input type='text' name='guess'/></p>
            <p><input type="submit"></p>
            </form>
            """

    response_object: Response = make_response(response_html)
    response_object.headers["Content-Type"] = "text/html"

    return response_object


@app.route("/dump", methods=["GET", "POST"])
def dump() -> Response:
    response_html: str = """
        <form method='post' action='/dump'>
        Zap Data: <input type="text" name="zap"><br/>
        Zot Data: <input type="text" name="zot"><br/>
        <input type="submit">
        </form>
        """

    environment_string: str = "<p><h1>Environment Dictionary:</h1><br/>"
    for variable_name, variable_value in request.environ.items():
        environment_string += f"{variable_name}: {variable_value}<br/>"

    environment_string += (
        f"<h1>Request Body Data</h1> <br/> {request.get_data(as_text=True)} </p>"
    )

    response_object: Response = make_response(response_html + environment_string)
    response_object.headers["Content-Type"] = "text/html"

    return response_object
