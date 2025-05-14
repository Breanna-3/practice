# DPR Project – Full Stack TV Show Explorer

## 📁 Project Structure

- **/notebooks/**
  - `01_database_setup.ipynb` – Sets up the normalized SQLite database with pandas + SQLite.
  - `02_api_tester.ipynb` – Tests external API (TVmaze) to gather and validate show data.

- **/flask_app/**
  - `app.py` – Flask backend with show filters and pagination.
  - `models.py` – SQLAlchemy object class for the TV show model.
  - `populate_db.py` – Downloads and saves shows from TVmaze into the SQLite DB.
  - `data.db` – SQLite database file.
  - **/static/images/** – Assets such as logos or creator profile images.
  - **/templates/** – Jinja2 templates: `index.html`, `creators.html`, `base.html`

- **/frontend/**
  - Starter directory for Astro project with React components (requires Node setup).

## 🛠 Technologies Used

- Python + Flask + SQLite (Backend)
- Astro + React (Frontend)
- TVmaze API (Data Source)
- Jupyter (Documentation & Testing)

## ✅ Features

- Browse & search TV shows by genre, type, country, etc.
- View paginated and sorted lists of popular shows
- Creator bio page with local images
- Fully normalized database setup
- API fetch & test notebooks
- React frontend integration plan

## 🚀 Setup Instructions

1. Clone this repo or unzip the files
2. Set up a Python environment and install requirements
3. Run `populate_db.py` to create your SQLite DB
4. Start Flask server via `python app.py`
5. (Optional) Navigate to `/frontend/` and run `npm install && npm run dev`

## 🧠 Author Notes

This project is designed for full-stack delivery of structured data via Python and visualization via Astro. It meets both technical and UX requirements for coursework or portfolio use.
