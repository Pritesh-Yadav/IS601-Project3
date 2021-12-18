from app.controllers.controller import ControllerBase
from flask import render_template


class zlayoutController(ControllerBase):
    @staticmethod
    def get():
        return render_template('zlayout.html')
