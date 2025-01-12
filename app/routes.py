from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
import joblib
import os
import numpy as np
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../trained_model.pkl")
model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        # numeric
        try:
            area = float(form.area.data)

            # ordinal
            bedrooms = int(form.bedrooms.data)
            bathrooms = int(form.bathrooms.data)
            stories = int(form.stories.data)
            parking = int(form.parking.data)

            # Binary Categorical
            mainroad = "yes" if int(form.mainroad.data) else "no"
            guestroom = "yes" if int(form.guestroom.data) else "no"
            basement = "yes" if int(form.basement.data) else "no"
            hotwaterheating = "yes" if int(form.hotwaterheating.data) else "no"
            airconditioning = "yes" if int(form.airconditioning.data) else "no"
            prefarea = "yes" if int(form.prefarea.data) else "no"

            furnishing_status = form.furnishing_status.data.strip().lower()

            features = pd.DataFrame(
                {
                    "area": [area],
                    "bedrooms": [bedrooms],
                    "bathrooms": [bathrooms],
                    "stories": [stories],
                    "mainroad": [mainroad],
                    "guestroom": [guestroom],
                    "basement": [basement],
                    "hotwaterheating": [hotwaterheating],
                    "airconditioning": [airconditioning],
                    "parking": [parking],
                    "prefarea": [prefarea],
                    "furnishingstatus": [
                        furnishing_status
                    ],  # Pass the raw furnishing status
                }
            )
            predicted_price = model.predict(features)

            # flash(f"Predicted House Price: ${predicted_price[0]:,.2f}", "success")

            return redirect(url_for("predict", price=predicted_price[0]))

        except ValueError as e:
            flash(f"Invalid input: {e}. Please check your entries.", "error")
            return redirect(url_for("index"))

    return render_template("index.html", form=form)


@app.route("/predict")
def predict():
    price = request.args.get("price", type=float)
    if price is None:
        flash("Prediction not available. Please try again.", "error")
    return render_template("predict.html", price=price)
