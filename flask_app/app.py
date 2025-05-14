from flask import Flask, render_template, request
from models import db, Show

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def index():
    shows = Show.query.limit(20).all()
    return render_template("index.html", shows=shows)

@app.route("/creators")
def creators():
    creators = [
        {"name": "Alice Kim", "bio": "Frontend designer.", "image": "/static/images/person1.jpg"},
        {"name": "Ben Patel", "bio": "Backend developer.", "image": "/static/images/person2.jpg"},
        {"name": "Chloe Zhang", "bio": "Full-stack engineer.", "image": "/static/images/person3.jpg"}
    ]
    return render_template("creators.html", creators=creators)

if __name__ == "__main__":
    app.run(debug=True)
