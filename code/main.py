from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
DB_NAME = "database.db"
app.config["SECRET_KEY"] = "3$Yh9K|@w2Z*bN-"
app.config["SQLALCHEMY_DATABASE_URI"]= f"sqlite:///{DB_NAME}"
db.init_app(app)

class Page(db.Model):
    name = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)

with app.app_context():
    db.create_all()

@app.route("/")
def site_index():
    return render_template("index.html")

@app.route("/page_creation", methods=["GET"])
def site_page_creation():
    return render_template("new_page.html")

@app.route("/pages/<page_name>", methods=["GET"])
def site_page_viewing(page_name):
    display_name = page_name.replace("-", " ").title()
    database_name = page_name.replace("-", " ").lower()

    try:
        page = Page.query.filter(Page.name == database_name).one()
        return render_template("page.html", page_name=page_name, display_name=display_name, description=page.description)
    except:
        return render_template("page_failure.html", page_name=page_name, display_name=display_name)

@app.route("/api/new_page", methods=["POST"])
def create_new_page():
    
    try:
        if "name" in request.json and "description" in request.json and len(request.json["name"]) > 0:
            name = request.json["name"].lower()
            page = Page(name=name, description=request.json["description"])
            db.session.add(page)
            db.session.commit()
            return "success"
    except:
        pass

    return "failure"

app.run(port=8080, debug=True)