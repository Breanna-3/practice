from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    summary = db.Column(db.Text)
    image = db.Column(db.String)
    genres = db.Column(db.String)
    genre_tag = db.Column(db.String)
    showType = db.Column(db.String)
    rating = db.Column(db.Float)
    premiered = db.Column(db.String)
    language = db.Column(db.String)
    runtime = db.Column(db.Integer)
    country = db.Column(db.String)
    network = db.Column(db.String)
