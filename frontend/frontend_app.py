from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SubmitField
import requests

#{"Wednesday": "08:00-08:30"}

api_url = "http://127.0.0.1:8086/api"

app = Flask(__name__)
app.secret_key = "supersecretkey"
csrf = CSRFProtect(app)

uuid = 1

class LogoutForm(FlaskForm):
    submit = SubmitField("Logout")

# Routes
@app.route("/")
def home():
    return render_template("index.html", api_base=api_url, uuid=uuid)

@app.route("/profile")
def profile():
    return render_template("profile.html", user=current_user)

@app.route("/settings")
def settings():
    return render_template("settings.html", user=current_user)

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

# Timetable dummy route
@app.route("/timetable")
def timetable_dashboard():
    return render_template("timetable.html", user=current_user)

# Grades dummy route
@app.route("/grades")
def grades_list():
    return "Grades List"

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", code=404, message="Site not found."), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("error.html", code=500, message="Internal Server error."), 500

if __name__ == "__main__":
    app.run(debug=False)
