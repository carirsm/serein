from flask import Blueprint, request, jsonify
from .models import MoodLog
from .database import db
from datetime import datetime

mood_bp = Blueprint("mood", __name__)

@mood_bp.route("/log", methods=["POST"])
def log_mood():
    print("POST /log hit")
    data = request.get_json()
    mood = data.get("mood")
    reason = data.get("reason")

    if not mood:
        return jsonify({"error": "Mood is required"}), 400
    
    new_log = MoodLog(
        mood=mood,
        reason=reason,
        created_at=datetime.utcnow()
    )
    db.session.add(new_log)
    db.session.commit()

    return jsonify({"message": "Mood logged successfully"}), 201

@mood_bp.route("/entries", methods=["GET"])
def get_entries():
    entries = MoodLog.query.order_by(MoodLog.created_at.desc()).all()
    return jsonify([
        {
            "id": entry.id,
            "mood": entry.mood,
            "reason": entry.reason,
            "timestamp": entry.created_at.isoformat()
        } for entry in entries
    ])
