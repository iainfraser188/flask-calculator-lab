from flask import render_template
from calculator_app import calculator


@calculator.routes('/')
def index():
    return render_template('index.html',calculator = 'home')