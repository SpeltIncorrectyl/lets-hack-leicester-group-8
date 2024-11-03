from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_socketio import SocketIO, emit
import sys

app = Flask(__name__)
db = SQLAlchemy()
DB_NAME = "database.db"
app.config["SECRET_KEY"] = "3$Yh9K|@w2Z*bN-"
app.config["SQLALCHEMY_DATABASE_URI"]= f"sqlite:///{DB_NAME}"
db.init_app(app)
socketio = SocketIO(app)

site = sys.argv[1]

class Page(db.Model):
    name = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String, db.ForeignKey("page.name"))
    content = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    likes = db.Column(db.Integer)
    reports = db.Column(db.Integer)

with app.app_context():
    db.create_all()

def is_it_true(value):
  return value.lower() == 'true'

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
    return_to_index = request.args.get("return_to_index", default=False, type=is_it_true)
    post_comment = request.args.get("post_comment", default=False, type=is_it_true)
    comments = Comment.query.filter(Comment.page == database_name).all()
    comments.reverse()
    comment_length = len(comments)

    try:
        page = Page.query.filter(Page.name == database_name).one()
        return render_template("page.html", page_name=page_name, display_name=display_name, database_name=database_name, description=page.description, site=site, return_to_index=return_to_index, post_comment=post_comment, comments=comments, comment_length=comment_length)
    except:
        return render_template("page_failure.html", display_name=display_name)
    
@app.route("/all_pages", methods=["GET"])
def site_all_page_viewing():
    pages = Page.query.all()
    page_names = [(page.name.title(), page.name.replace(" ", "-").lower()) for page in pages]
    return render_template("all_pages.html", page_names=page_names)

@app.route("/api/post_comment", methods=["POST"])
def api_post_comment():
    #page, content
    # try:
    if "page" in request.json and "content" in request.json and len(request.json["content"]) > 0:
        _page = Page.query.filter(Page.name == request.json["page"]).one()

        comment = Comment(page=request.json["page"], content = request.json["content"], date=datetime.strftime(datetime.now(), "%d-%m-%Y"), time=datetime.strftime(datetime.now(), "%H:%M:%S"), likes=0, reports=0)
        socketio.emit("comments_changed", {"page": request.json["page"]})
        db.session.add(comment)
        db.session.commit()
        return "success", 200
    # except:
    #     pass

    return "Failed to publish comment.", 400

@app.route("/api/new_page", methods=["POST"])
def api_create_new_page():
    # name, description
    try:
        if "name" in request.json and "description" in request.json and len(request.json["name"]) > 0:
            database_name = request.json["name"].lower()
            url_name = request.json["name"].replace(" ", "-").lower()
            page = Page(name=database_name, description=request.json["description"])
            db.session.add(page)
            db.session.commit()
            return url_name, 200
        else:
            return "Invalid form data.", 400
    except:
        return "Page already exists.", 400

app.run(port=8080, debug=True)