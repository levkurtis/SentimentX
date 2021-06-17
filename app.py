from flask import Flask, redirect, url_for, render_template, request
import twitterAPI

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        result = request.form["search"]
        return redirect(url_for("result", res=result))
    else:
        return render_template("index.html")

@app.route("/<res>", methods=["POST", "GET"])
def result(res):
    query_result = twitterAPI.main(res)
    website = f"<h1>This is your results</h1><h2>{query_result[2]}</h2>"

    return website
    
    

