# 🌧️ Serein — Mood Tracker App

**Serein** is a personal mood tracking web app built with **HTML** & **CSS**, **Python (Flask)** and **PostgreSQL**, designed to help users log their daily emotional state, reflect on their experiences, and gain insights into their mental health patterns over time.

> _"Serein" is the fine, light rain that falls from a clear sky after the cloudy weather, reflecting that peaceful after a storm, that no matter how tough it gets, all it is in the end is just a moment._

---

## 🛠️ Tech Stack

- **Frontend:** HTML, Jinja templates, CSS (WIP)
- **Backend:** Python (Flask)
- **Database:** PostgreSQL
- **ORM:** Flask SQLAlchemy

---

## ✨ Features (Work In Progress)

- ✅ Log a daily mood (e.g. Happy, Sad, Neutral) with an optional reason
- ✅ Store logs in a PostgreSQL database with timestamp
- ✅ View logged moods in a readable format with human-friendly dates
- 🔜 Auto-refresh and live feedback (Toast notifications planned)
- 🔜 Filter moods by week/month
- 🔜 Graph mood trends over time

---

## 🧠 Goals

This project is designed to:

- Practice real-world **CRUD** operations using Flask and PostgreSQL
- Build strong database integration habits with SQLAlchemy
- Create a **safe space** for users to reflect on their emotional history
- Encourage **daily journaling** and self-awareness through simple UI/UX

---

## 🚀 Getting Started (Local Setup)

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/serein.git
   cd serein

3. Setup your virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

5. Install dependencies:
    ```bash
   pip install -r requirements.txt

7. Setup your .env file or update config.py with your PostgreSQL connection:
    ```bash
     DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/serein_db

9. Initialize the database:
    ```bash
    flask shell
    >>> from app import db, create_app
    >>> app = create_app()
    >>> with app.app_context():
    ...     db.create_all()

6. Run the app:
    ```bash
    flask run

## 👨‍💻 Author

**Oscar Paul Perez**  
Aspiring Software Engineer with a background in dispatch and logistics coordination.  
[LinkedIn](https://www.linkedin.com/in/oscarpaulperez/)  
[GitHub](https://github.com/carirsm)

---

## 📄 License

This project is licensed under the MIT License.
