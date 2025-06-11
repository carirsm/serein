import os

# database settings - change database name later - update link as well
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(basedir, 'serein.db')}"
