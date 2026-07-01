from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home_page():
    return render_template("home.html")

@views.route('/quotes')
def get_quotes():
    return "<h1>Get Quotes Here!!</h1>"

@views.route('/mood-jar')
def mood_jar():
    return "<h1>Mood Jar Here!!"

@views.route('/mood-tracker')
def mood_tracker():
    return "<h1>Mood Tracker Here!!"