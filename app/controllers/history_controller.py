from app.controllers.controller import ControllerBase
from flask import render_template


class history(ControllerBase):
    @staticmethod
    def get():
        return render_template('history.html')