class Feedback(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.String)
    comment = db.Column(db.String)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)