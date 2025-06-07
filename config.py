import os

# database settings - change database name later
DATABASE_URL = os.environ.get("DATABASE_URL") or "postgresql://your_user:your_password@localhost/serein_db"
