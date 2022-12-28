from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password=password):
                flash('Logged in successfully !', category='success')
                login_user(user=user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password !', category='error')
        else:
            flash('email does not exists', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists !', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 character', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characers', category='error')
        elif password != password_confirm:
            flash('password and confirm aren\'t the same', category='error')
        elif len(password) < 7:
            flash('password should have at least 7 character long', category='error')
        else:
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user=user, remember=True)
            flash('Account created !', category='success')
            return redirect(url_for('views.home'))

    return render_template('register.html', user=current_user)