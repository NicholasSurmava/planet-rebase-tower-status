import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('tower_status', __name__, template_folder='templates/tower_status')

@bp.route('/tower_status')
def index():
    return 'tower status'

@bp.route('/tower_status/report')
def tower_status_report():
    return 'site status report'