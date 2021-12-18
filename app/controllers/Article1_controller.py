from app.controllers.controller import ControllerBase
from flask import render_template

class Article1controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('Article1.html')
