from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import models

db = SQLAlchemy()
DB_NAME = "database.db"  
app = Flask(__name__)
# socketio = SocketIO()

app.config["SECRET_KEY"] = "3$Yh9K|@w2Z*bN-"
app.config["SQLALCHEMY_DATABASE_URI"]= f"sqlite:///{DB_NAME}"
db.init_app(app)

class Feedback(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.String)
    comment = db.Column(db.String)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)


with app.app_context():
    db.create_all()


@app.route("/",methods=["GET","POST"])
def main():
    if request.method == "POST":
        pass
    return render_template("index.html")


# @socketio.on('')
# def delete_item(id):


app.run(host="0.0.0.0",port=80,debug=True)
