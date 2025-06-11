from .database import db
from datetime import datetime

class MoodLog(db.Model):
    __tablename__ = 'mood_logs'

    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(10), nullable=False)
    reason = db.Column(db.Text)
    date = db.Column(db.Date, default=datetime.utcnow().date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    
