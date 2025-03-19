from flask import Flask, Blueprint, render_template, url_for

web_bp = Blueprint('web', __name__, url_prefix='/')


@web_bp.route('/')
def main_page():
    return render_template('main_page.html')

@web_bp.route('/login')
def log_in():
    return render_template('log_in.html')

@web_bp.route('/signup')
def sign_up():
    return render_template('sign_up.html')

@web_bp.route('/mainmsg')
def main_msg():
    return render_template('main_msg.html')
