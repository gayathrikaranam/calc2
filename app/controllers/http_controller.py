from app.controllers.controller import ControllerBase
from flask import render_template


class http(ControllerBase):
    @staticmethod
    def get():
        return render_template('http.html')
