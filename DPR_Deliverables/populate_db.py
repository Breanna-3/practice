import requests
import pandas as pd
from flask_app.models import db, Show
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    response = requests.get("https://api.tvmaze.com/shows?page=0")
    data = response.json()

    for item in data[:50]:
        show = Show(
            id=item["id"],
            name=item["name"],
            summary=item.get("summary"),
            image=item["image"]["medium"] if item.get("image") else None,
            genres=",".join(item.get("genres", [])),
            genre_tag=item["genres"][0] if item.get("genres") else "Unknown",
            showType=item.get("type", "Unknown"),
            rating=item["rating"]["average"] if item.get("rating") else None,
            premiered=item.get("premiered"),
            language=item.get("language"),
            runtime=item.get("runtime"),
            country=item["network"]["country"]["name"] if item.get("network") and item["network"].get("country") else None,
            network=item["network"]["name"] if item.get("network") else None
        )
        db.session.add(show)
    db.session.commit()
