from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint("info", __name__)

@bp.route("/")
def index():
    return "homepage"
