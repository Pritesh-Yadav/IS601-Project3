from app.controllers.controller import ControllerBase
from flask import render_template


class Article2controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('Article2.html')
