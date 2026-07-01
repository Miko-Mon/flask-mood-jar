from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home_page():
    return render_template("home.html", title="Homepage")

@views.route('/quotes')
def get_quotes():
    return render_template("quotes.html", title="Quotes")

@views.route('/mood-jar')
def mood_jar():
    return render_template("mood_jar.html", title="Mood Jar")

@views.route('/mood-tracker')
def mood_tracker():
    return render_template("mood_tracker.html", title="Mood Tracker")