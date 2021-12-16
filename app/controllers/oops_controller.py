from app.controllers.controller import ControllerBase
from flask import render_template


class oops(ControllerBase):
    @staticmethod
    def get():
        return render_template('OOPS.html')
