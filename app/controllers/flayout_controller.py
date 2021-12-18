from app.controllers.controller import ControllerBase
from flask import render_template


class flayoutController(ControllerBase):
    @staticmethod
    def get():
        return render_template('flayout.html')
