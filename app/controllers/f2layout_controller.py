from app.controllers.controller import ControllerBase
from flask import render_template


class f2layout(ControllerBase):
    @staticmethod
    def get():
        return render_template('f2layout.html')
