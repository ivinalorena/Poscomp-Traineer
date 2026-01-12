from flask import Blueprint, render_template, request, redirect,url_for

user_bp = Blueprint('user',__name__,static_folder='static',template_folder='templates')

@user_bp.route('/dash')
def dash():
    return '''<h1> olá mundo</h1>'''