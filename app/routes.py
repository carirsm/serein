from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from .models import MoodLog
from .database import db
from datetime import datetime

mood_bp = Blueprint("mood", __name__)

@mood_bp.route("/", methods=["GET"])
def home():
    return render_template("log_mood.html")

@mood_bp.route("/log", methods=["POST"])
def log_mood():
    if request.is_json:
        data = request.get_json()
        mood = data.get("mood")
        reason = data.get("reason")
    else:
        mood = request.form.get("mood")
        reason = request.form.get("reason")

    if not mood:
        return jsonify({"error": "Mood is required"}), 400

    new_log = MoodLog(mood=mood, reason=reason)
    db.session.add(new_log)
    db.session.commit()

    if request.is_json:
        return jsonify({"message": "Mood logged successfully!"}), 201
    else:
        return redirect(url_for("mood.get_entries"))

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
