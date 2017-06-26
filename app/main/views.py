from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')