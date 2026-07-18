from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home_page():
    return render_template("home.html", title="Homepage", user = current_user)

@views.route('/quotes')
def get_quotes():
    return render_template("quotes.html", title="Quotes", user = current_user)

@views.route('/mood-jar')
@login_required
def mood_jar():
    return render_template("mood_jar.html", title="Mood Jar", user = current_user)

@views.route('/mood-tracker')
@login_required
def mood_tracker():
    return render_template("mood_tracker.html", title="Mood Tracker", user = current_user)