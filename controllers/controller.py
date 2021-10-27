from flask import render_template
from calculator_app import calculator_app
from modules.calculator import *

@calculator_app.route('/')
def index():
   return 'hello world'


@calculator_app.route('/add/<num1>/<num2>')
def addition(num1,num2):
    return f' the answer is {add(int(num1),int(num2))}'

@calculator_app.route('/subtract/<num1>/<num2>')
def subtraction(num1,num2):
    return f' the answer is {subtract(int(num1),int(num2))}'
    
@calculator_app.route('/multiply/<num1>/<num2>')
def multiplcation(num1,num2):
    return f' the answer is {multiply(int(num1),int(num2))}'
    
@calculator_app.route('/divide/<num1>/<num2>')
def division(num1,num2):
    return f' the answer is {divide(int(num1),int(num2))}'