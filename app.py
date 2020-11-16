import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/characters")
def characters():
    characters = mongo.db.characters.find()
    return render_template("characters.html", characters=characters)


@app.route("/new_character", methods=["GET", "POST"])
def new_character():

    if request.method == "POST":

        if "chosen_class" in request.form:
            chosen_class = {
                "class_name": request.form.get("class_name"),
                "class_hit_die": request.form.get("class_hit_die"),
                "class_skill_prof": request.form.get("class_skill_prof")
            }
        elif "chosen_race" in request.form:
            chosen_race = {
                "race_name": request.form.get("race_name"),
                "race_size": request.form.get("race_size"),
                "race_speed": request.form.get("race_speed"),
                "race_languages": request.form.get("race_languages")
            }
        elif "chosen_background" in request.form:
            chosen_background = {
                "background_languages": request.form.get(
                    "background_languages"),
                "background_name": request.form.get("background_name"),
                "background_prof": request.form.get("background_prof"),
                "background_equipment": request.form.get(
                    "background_equipment")
            }
        else:
            character = {
                **chosen_class,
                **chosen_race,
                **chosen_background
            }

            mongo.db.characters.insert_one(character)

    classes = list(mongo.db.classes.find())
    races = mongo.db.races.find()
    backgrounds = mongo.db.backgrounds.find()
    return render_template("new_character.html",
        classes=classes, races=races, backgrounds=backgrounds)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username")
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username")
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab session user's username for the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect("login")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)