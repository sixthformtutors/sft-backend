from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .db import get_db

bp = Blueprint("admin", __name__, url_prefix="/admin")

@bp.route("/")
def index():
    if session.get("admin_key") is None:
        return redirect("admin.login")
    return redirect("admin.panel")

@bp.route("/login")
def login():
    return "todo"

@bp.route("/panel")
def panel():
    db = get_db()
    users = db.execute("SELECT * FROM users")
    return render_template("admin/panel.html", users=users)
