from flask import render_template
from calculator_app import calculator_app
from modules.calculator import *

# @calculator_app.route('/')
# def index():
#    return 'hello world'


@calculator_app.route('/add/<num1>/<num2>')
def addition(num1,num2):
    answer = add(int(num1),int(num2))
    return render_template('index.html',calculator= 'home', answer = answer)

    # return f' the answer is {add(int(num1),int(num2))}'

@calculator_app.route('/subtract/<num1>/<num2>')
def subtraction(num1,num2):
    answer = subtract(int(num1),int(num2))
    return render_template('index.html',calculator= 'home', answer = answer)
    
@calculator_app.route('/multiply/<num1>/<num2>')
def multiplcation(num1,num2):
  answer = multiply(int(num1),int(num2))
  return render_template('index.html',calculator= 'home', answer = answer)    


@calculator_app.route('/divide/<num1>/<num2>')
def division(num1,num2):
    answer = divide(int(num1),int(num2))
    return render_template('index.html',calculator= 'home', answer = answer)