from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home_page():
    return render_template("home.html")

@views.route('/get-quotes')
def get_quotes():
    return "<h1>Get Quotes Here!!</h1>"

@views.route('/add-quotes')
def add_quotes():
    return "<h1>Add Quotes Here!</h1>"