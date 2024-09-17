from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()

        try:
            db.execute(
                "INSERT INTO users (username, password) VALUES(?, ?)",
                (username, generate_password_hash(password))
            )
            db.commit()
        except db.IntegrityError:
            flash(f"User '{username}' is already registered.")
        else:
            return redirect(url_for("auth.login"))

    return render_template("auth/register.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
    return "todo"
