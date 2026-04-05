from flask import Flask, render_template, request, redirect, url_for, flash, session
import pandas as pd
import functions as f
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "your_secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chalaksetu_user:zVzQNRcri49z4aqBvRzAvDtgZhRZncAf@dpg-d06cfmruibrs73eeoibg-a.ohio-postgres.render.com/chalaksetu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(15))  # optional
    password = db.Column(db.Text, nullable=False)

with app.app_context():
    db.drop_all()    # ⚠️ Old table + data will be deleted
    db.create_all()  # ✅ New table (with correct structure) will be created

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            flash("Login successful!", "success")
            return redirect(url_for('welcome'))
        flash("Invalid username or password.", "error")
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("signup"))

        otp, notice = f.send_email(email)
        session.update({
            "otp": str(otp),
            "username": username,
            "email": email,
            "phone": phone,
            "password": password
        })

        flash(notice, "info")
        return redirect(url_for("verify_otp"))
    return render_template("signup.html")

@app.route("/verify_otp", methods=["GET", "POST"])
def verify_otp():
    if request.method == "POST":
        user_otp = request.form.get("otp")
        if user_otp.strip() == session.get("otp"):
            try:
                new_user = User(
                    username=session["username"],
                    email=session["email"],
                    phone=session.get("phone"),
                    password=session["password"]
                )
                db.session.add(new_user)
                db.session.commit()
                flash("Account created successfully!", "success")
                return redirect(url_for("index"))
            except:
                db.session.rollback()
                flash("An error occurred. Try a different username or email.", "error")
                return redirect(url_for("signup"))
        flash("Incorrect OTP.", "error")
    return render_template("verify_otp.html")

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            otp, notice = f.send_email(email)
            session.update({
                "reset_otp": str(otp),
                "reset_user_id": user.id
            })
            flash(notice, "info")
            return redirect(url_for("verify_reset_otp"))
        flash("Email not found.", "error")
    return render_template("forgot_password.html")

@app.route("/verify_reset_otp", methods=["GET", "POST"])
def verify_reset_otp():
    if request.method == "POST":
        user_otp = request.form.get("otp")
        if user_otp.strip() == session.get("reset_otp"):
            return redirect(url_for("reset_password"))
        flash("Incorrect OTP.", "error")
    return render_template("verify_reset_otp.html")

@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("reset_password"))

        user = User.query.get(session.get("reset_user_id"))
        if user:
            user.password = password
            db.session.commit()
            flash("Password reset successfully.", "success")
            return redirect(url_for("index"))
        flash("Something went wrong.", "error")
    return render_template("reset_password.html")

@app.route("/welcome")
def welcome():
    df = pd.read_csv("datasets/indian_cities_coordinates.csv")
    city_ = list(df["City Name"])
    city_.insert(0, "My Current Location")
    return render_template("welcome.html", city=city_, mechanics_list=[])

@app.route("/start", methods=["POST"])
def start():
    df = pd.read_csv("datasets/indian_cities_coordinates.csv")
    selected_city = request.form.get("selected_city")
    city_ = list(df["City Name"])
    city_.insert(0, "My Current Location")

    mechanics_list = []
    if selected_city:
        flash(f"You selected: {selected_city}", "success")
        mechanics_list = f.near_mechnics(selected_city, df)
    else:
        flash("No city selected!", "error")

    return render_template("welcome.html", city=city_, mechanics_list=mechanics_list)

if __name__ == "__main__":
    app.run(debug=True)
