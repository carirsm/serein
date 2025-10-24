from flask import Blueprint, request, jsonify, redirect, url_for, render_template, flash, session, current_app
from datetime import datetime, timedelta
from sqlalchemy import desc
from .models import MoodLog
from .database import db
import os

mood_bp = Blueprint("mood", __name__)

@mood_bp.before_request
def before_request():
    if 'user_id' not in session:
        session['user_id'] = os.urandom(24).hex()

# Home Route
@mood_bp.route("/", methods=["GET"])
def home():
    print("HOME route accessed")
    print(f"Template folder: {current_app.template_folder}")
    return render_template("log_mood.html")

# Log Mood Route
@mood_bp.route("/log", methods=["POST"])
def log_mood():
    print("LOG route accessed")
    print(f"Request method: {request.method}")
    mood = request.form.get("mood")
    reason = request.form.get("reason")

    if not mood:
        flash("Mood is required.", "error")
        print("Flash error message")
        return redirect(url_for("mood.home"))

    new_log = MoodLog(mood=mood, reason=reason)
    db.session.add(new_log)
    db.session.commit()

    flash("Mood logged successfully!", "success")
    print("Flashed success message")
    return redirect(url_for("mood.home"))

# JSON Entry List Route
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

# View Moods Route
@mood_bp.route("/view")
def view_moods():
    if 'user_id' not in session:
        session['user_id'] = os.urandom(24).hex()

    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    date_filter = request.args.get('date_filter', 'all')
    
    query = MoodLog.query

    if date_filter == 'today':
        query = query.filter(MoodLog.date == datetime.now().date())
    elif date_filter == 'week':
        week_ago = datetime.now().date() - timedelta(days=7)
        query = query.filter(MoodLog.date >= week_ago)
    elif date_filter == 'month':
        month_ago = datetime.now().date() - timedelta(days=30)
        query = query.filter(MoodLog.date >= month_ago)

    entries = query.order_by(desc(MoodLog.created_at)).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template(
        'mood_entries.html',
        entries=entries,
        date_filter=date_filter
    )

# mood stats route
@mood_bp.route("/stats")
def mood_stats():
    moods = MoodLog.query.all()
    total = len(moods)
    if total > 0:
        good_count = sum(1 for m in moods if m.mood == "good")
        neutral_count = sum(1 for m in moods if m.mood == "neutral")
        bad_count = sum(1 for m in moods if m.mood == "bad")

        data = {
            "good": round((good_count / total) * 100, 1),
            "neutral": round((neutral_count / total) * 100, 1),
            "bad": round((bad_count / total) * 100, 1),
        }

    else:
        data = {"good": 0, "neutral": 0, "bad": 0}

    return render_template("mood_stats.html", data=data)