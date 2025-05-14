# 🎬 TV Show Explorer Project

This project allows users to explore TV shows using a Flask backend connected to a SQLite database and an Astro/React frontend.

## 📁 Project Structure

```
tv_project/
├── api/
│   ├── app.py                # Flask application
│   ├── tools.py              # SQLite helper tools
│   ├── populate_db.py        # Downloads data from TVmaze API
│   └── templates/            # HTML templates for Flask
│       ├── base.html
│       ├── index.html
│       ├── show.html
│       └── creators.html
├── frontend/
│   └── src/
│       ├── components/
│       │   └── ShowCard.jsx  # React component for shows
│       └── pages/
│           └── index.astro   # Home page to render shows
├── notebooks/
│   ├── setup_database.ipynb  # (Optional) Setup notebook
│   └── api_tester.ipynb      # (Optional) API test notebook
└── data.csv                  # Exported data from TVmaze
```

## ✅ Setup Instructions

### 1. Install Python dependencies
```bash
pip install flask flask_sqlalchemy flask_migrate pandas requests
```

### 2. Run Data Population
```bash
cd api
python populate_db.py
```

### 3. Start Flask App
```bash
python app.py
```
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 4. Astro Frontend (Optional)

#### Prerequisite: Node.js

```bash
cd frontend
npm create astro@latest
npm install
npm run dev
```

Ensure Flask is running on port 5000 for frontend to fetch data.

---

## 📚 Features
- Filter by genre, language, runtime, network, country, show type
- Sort shows by popularity, rating, release
- Show detail page
- Creators page

---

## 👩‍💻 Authors
- Ammal, Breanna, Chloe Zhang

---

## 🗃️ Data Source
Powered by [TVmaze API](https://www.tvmaze.com/api)

