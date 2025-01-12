from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = LoginForm()
    # if form.validate_on_submit
    return render_template("index.html", form = form)
