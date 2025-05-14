from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from tools import DB
import os
import threading
import webbrowser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

tv_db = DB("data")

@app.route('/')
def index():
    all_genres = sorted([
        row['genre_tag'] for _, row in tv_db.query(
            "SELECT DISTINCT genre_tag FROM shows WHERE genre_tag IS NOT NULL"
        ).iterrows() if row['genre_tag'] != 'Unknown'
    ])

    all_show_types = sorted([
        row['showType'] for _, row in tv_db.query(
            "SELECT DISTINCT showType FROM shows WHERE showType IS NOT NULL"
        ).iterrows()
    ])

    # Get filters
    genre_filter = request.args.get('genre', '')
    show_type = request.args.get('showType', '')
    sort_by = request.args.get('sort', 'popularity')
    year = request.args.get('year', '')
    language = request.args.get('language', '')
    country = request.args.get('country', '')
    runtime = request.args.get('runtime', '')
    network = request.args.get('network', '')
    page = int(request.args.get('page', 1))
    shows_per_page = 24
    offset = (page - 1) * shows_per_page

    sort_column = {
        'name': 'name COLLATE NOCASE ASC',
        'popularity': 'rating DESC',
        'release': 'premiered DESC',
        'highest': 'rating DESC',
        'lowest': 'rating ASC'
    }.get(sort_by, 'name COLLATE NOCASE ASC')

    query = "SELECT * FROM shows WHERE 1=1"
    count_query = "SELECT COUNT(*) as count FROM shows WHERE 1=1"
    params = {}
    count_params = {}

    if genre_filter:
        query += " AND genre_tag = :g"
        count_query += " AND genre_tag = :g"
        params["g"] = count_params["g"] = genre_filter

    if show_type:
        query += " AND showType = :s"
        count_query += " AND showType = :s"
        params["s"] = count_params["s"] = show_type

    if year:
        query += " AND premiered LIKE :y"
        count_query += " AND premiered LIKE :y"
        params["y"] = count_params["y"] = f"{year}%"

    if language:
        query += " AND language = :l"
        count_query += " AND language = :l"
        params["l"] = count_params["l"] = language

    if country:
        query += " AND country = :c"
        count_query += " AND country = :c"
        params["c"] = count_params["c"] = country

    if network:
        query += " AND network = :n"
        count_query += " AND network = :n"
        params["n"] = count_params["n"] = network

    if runtime:
        if runtime == "short":
            query += " AND runtime <= 30"
            count_query += " AND runtime <= 30"
        elif runtime == "medium":
            query += " AND runtime > 30 AND runtime <= 60"
            count_query += " AND runtime > 30 AND runtime <= 60"
        elif runtime == "long":
            query += " AND runtime > 60"
            count_query += " AND runtime > 60"

    query += f" ORDER BY {sort_column} LIMIT {shows_per_page} OFFSET {offset}"

    df = tv_db.query(query, params)
    shows = df.to_dict(orient='records')

    count_df = tv_db.query(count_query, count_params)
    total_shows = count_df.iloc[0]['count']
    total_pages = (total_shows + shows_per_page - 1) // shows_per_page

    years = [row['year'] for _, row in tv_db.query(
        "SELECT DISTINCT substr(premiered, 1, 4) as year FROM shows WHERE premiered IS NOT NULL ORDER BY year DESC"
    ).iterrows() if row['year']]

    languages = [row['language'] for _, row in tv_db.query(
        "SELECT DISTINCT language FROM shows WHERE language IS NOT NULL ORDER BY language"
    ).iterrows()]

    countries = [row['country'] for _, row in tv_db.query(
        "SELECT DISTINCT country FROM shows WHERE country IS NOT NULL ORDER BY country"
    ).iterrows()]

    networks = [row['network'] for _, row in tv_db.query(
        "SELECT DISTINCT network FROM shows WHERE network IS NOT NULL ORDER BY network"
    ).iterrows()]

    return render_template("index.html",
                           shows=shows,
                           genres=all_genres,
                           show_types=all_show_types,
                           selected_genre=genre_filter,
                           selected_show_type=show_type,
                           selected_sort=sort_by,
                           selected_year=year,
                           selected_language=language,
                           selected_country=country,
                           selected_runtime=runtime,
                           selected_network=network,
                           years=years,
                           languages=languages,
                           countries=countries,
                           networks=networks,
                           current_page=page,
                           total_pages=total_pages)

@app.route('/show/<int:show_id>')
def show_detail(show_id):
    df = tv_db.query("SELECT * FROM shows WHERE id = :id", {"id": show_id})
    if df.empty:
        return "Show not found", 404
    show = df.iloc[0].to_dict()
    return render_template("show.html", show=show)

@app.route('/search')
def search():
    q = request.args.get('q', '')
    results = []
    if q:
        df = tv_db.query("SELECT * FROM shows WHERE name LIKE :q", {"q": f"%{q}%"})
        results = df.to_dict(orient='records')
    return render_template("index.html", shows=results,
                           genres=[], show_types=[],
                           selected_genre="", selected_show_type="",
                           selected_sort="name", selected_year="",
                           selected_language="", selected_country="",
                           selected_runtime="", selected_network="",
                           years=[], languages=[], countries=[], networks=[],
                           current_page=1, total_pages=1)

@app.route('/creators')
def creators():
    creators = [
        {
            "name": "Ammal",
            "bio": "Frontend designer and UX lover. Makes things pretty and usable.",
            "image": "/static/images/person1.jpg"
        },
        {
            "name": "Breanna",
            "bio": "Backend architect with a passion for clean APIs and strong data.",
            "image": "/static/images/person2.jpg"
        },
        {
            "name": "Chloe Zhang",
            "bio": "Code wrangler and database whisperer. Also does cats and coffee.",
            "image": "/static/images/person3.jpg"
        }
    ]
    return render_template("creators.html", creators=creators)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)
