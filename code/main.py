from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_page", methods=["GET"])
def new_page():
    return render_template("new_page.html")

@app.route("/new_page/creation", methods=["POST"])
def create_new_page():
    if request.method == "POST":
        print(request.form["name"])
    return "Success!"

app.run(port=8080, debug=True)