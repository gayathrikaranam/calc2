from app.controllers.controller import ControllerBase
from flask import render_template


class flayout(ControllerBase):
    @staticmethod
    def get():
        return render_template('flayout.html')
