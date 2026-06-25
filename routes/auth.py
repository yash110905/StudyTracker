from flask import Blueprint, render_template, request, redirect
from database import db
from models.user import User
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user


auth = Blueprint("auth", __name__)
bcrypt = Bcrypt()# Initialize password


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password) #Hash password and create new user
        user = User(
            email=email,
            password=hashed_password
        )
        db.session.add(user)#Save user to database
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")#Show registration page


@auth.route("/login", methods=["GET", "POST"])
def login():#login form submission

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(
            user.password,
            password
        ):
            login_user(user)
            return "Logged in successfully"#Log user in
    return render_template("login.html")

@auth.route("/logout")
def logout():

    logout_user()#Log user out

    return redirect("/login")