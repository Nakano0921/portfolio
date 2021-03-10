from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user

from portfolio.forms import LoginForm, SignupForm
from portfolio.models import Restaurant

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        restaurant = Restaurant.select_by_email(form.email.data)
        if restaurant and restaurant.validate_password(form.password.data):
            login_user(restaurant)
            return render_template('toppage.html')
    return render_template('home.html', form=form)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        restaurant = Restaurant(
            email = form.email.data,
            restaurant = form.restaurant.data,
            password = form.password.data
        )
        restaurant.add_user()
        return redirect(url_for('app.login'))
    return render_template('signup.html', form=form)
