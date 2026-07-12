from flask import Blueprint, render_template, request, flash, redirect, url_for
import re

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", title="Login")

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

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

        # Database Operation here: Pending

        flash("Account successfully created!", "success")

        return redirect(url_for('auth.login'))

    return render_template("sign_up.html", title="Sign-up")