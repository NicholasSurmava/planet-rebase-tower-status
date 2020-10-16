import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form["user"]
        password = request.form['password']

        session["user"] = user
        print(user)

        # TODO: After logging in, redirect to the route the user originally requested, ?next=/site_report
        return redirect(url_for("tower_status.index", user=user))
    
    return render_template('login.html')

@bp.route('/logout')
def logout():
    return 'logout'