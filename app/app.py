"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.Article1_controller import Article1controller
from app.controllers.Article2_controller import Article2controller
from app.controllers.zlayout_controller import zlayoutController
from app.controllers.flayout_controller import flayoutController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()


@app.route("/basicform", methods=['GET'])
def calculator_get():
    return CalculatorController.get()


@app.route("/basicform", methods=['POST'])
def calculator_post():
    return CalculatorController.post()


@app.route("/zlayout", methods=['GET'])
def zlayout_get():
    return zlayoutController.get()


@app.route("/Article1", methods=['GET'])
def Article1_get():
    return Article1controller.get()


@app.route("/Article2", methods=['GET'])
def Article2_get():
    return Article2controller.get()


@app.route("/flayout", methods=['GET'])
def flayout_get():
    return flayoutController.get()
