from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, {escape(name)}!</p>"

name = "Levent"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')