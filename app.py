import os

from flask import Flask, jsonify, render_template


# Import API Keys


is_prod = os.environ.get('IS_HEROKU', None)

API_KEY = os.environ['API_KEY']


app = Flask(__name__)



@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run()