from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from sqlalchemy import or_
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username_or_email = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter(
            or_(
                User.username == username_or_email,
                User.email == username_or_email.lower()
            )
        ).first()

        if not user:
            flash("This user does not exist, please check if username/email is correct.", "error")
            return render_template("login.html", title="Login")

        if not check_password_hash(user.password, password):
            flash("Wrong password. Please try again.", "error")
            return render_template("login.html", title="Login")

        # When login is successful
        flash("Logged in successfully!", "success")
        login_user(user, remember=True)
        return redirect(url_for('views.home_page'))

    return render_template("login.html", title="Login", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    # Thing to add: Make it so that it automatically checks the username and email before clicking the sign-up button

    if request.method == 'POST':
    
    # Clean input
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Validation: Username
        if not username:
            flash("Username is required.", "error")
            return render_template("sign_up.html", title="Sign-up")

        if len(username) < 3:
            flash("Username must be at least 3 characters long.", "error")
            return render_template("sign_up.html", title="Sign-up")

        # Validation: Email
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(email_pattern, email):
            flash("Please enter a valid email address.", "error")
            return render_template("sign_up.html", title="Sign-up")

        # Validation: Password
        if len(password) < 8:
            flash("Password must be at least 8 characters long.", "error")
            return render_template("sign_up.html", title="Sign-up")

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("sign_up.html", title="Sign-up")
        
        existing_user = User.query.filter(
            or_(
                User.username == username,
                User.email == email
            )
        ).first()

        if existing_user:
            if existing_user.username == username:
                flash("Username is already taken.", "error")
            elif existing_user.email == email:
                flash("This email is already registered", "error")

            return render_template("sign_up.html", title="Sign-up")

        # Database Operation: Adding a new user
        new_user = User(email=email, username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        flash("Account successfully created!", "success")

        return redirect(url_for('auth.login'))

    return render_template("sign_up.html", title="Sign-up", user=current_user)