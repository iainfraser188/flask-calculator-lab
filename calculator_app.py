from flask import Flask

calculator_app = Flask(__name__)

from controllers import controller

if __name__ == '__main__':
    calculator_app.run(debug=True)