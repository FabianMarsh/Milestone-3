import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
import math
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


@app.route("/get_modifier")
def get_modifier(stat):
    int(stat)

    modifier = (stat - 10) / 2
    modifier = math.floor(modifier)

    return modifier


@app.route("/new_character", methods=["GET", "POST"])
def new_character():

    if request.method == "POST":

        if "class" in request.form:

            index = request.form.get("class")

            session["class"] = {
                "class_name": request.form.get("class_name_" + index),
                "class_hit_die": request.form.get("class_hit_die_" + index),
                "class_skill_prof": request.form.get(
                    "class_skill_prof_" + index)
            }

        if "race" in request.form:

            index = request.form.get("race")

            session["race"] = {
                "race_name": request.form.get("race_name_" + index),
                "race_size": request.form.get("race_size_" + index),
                "race_speed": request.form.get("race_speed_" + index),
                "race_languages": request.form.get("race_languages_" + index)
            }

        if "background" in request.form:

            index = request.form.get("background")

            session["details"] = {
                "background_name": request.form.get(
                    "background_name_" + index),
                "background_languages": request.form.get(
                    "background_languages_" + index),
                "background_skill_prof": request.form.get(
                    "background_skill_prof_" + index),
                "background_equipment": request.form.get(
                    "background_equipment_" + index),
                "character_name": request.form.get("character_name")
                }

        if "ability_scores" in request.form:
            session["ability"] = {
                "strength": int(request.form.get("strength")),
                "strength_modifier": get_modifier(
                    int(request.form.get("strength"))),
                "dexterity": int(request.form.get("dexterity")),
                "dexterity_modifier": get_modifier(
                    int(request.form.get("dexterity"))),
                "constitution": int(request.form.get("constitution")),
                "constitution_modifier": get_modifier(
                    int(request.form.get("constitution"))),
                "intelligence": int(request.form.get("intelligence")),
                "intelligence_modifier": get_modifier(
                    int(request.form.get("intelligence"))),
                "wisdom": int(request.form.get("wisdom")),
                "wisdom_modifier": get_modifier(
                    int(request.form.get("strength"))),
                "charisma": int(request.form.get("charisma")),
                "charisma_modifier": get_modifier(
                    int(request.form.get("charisma"))),
            }

        if "submit" in request.form:

            character = {
                **session.get("class"),
                **session.get("race"),
                **session.get("details"),
                **session.get("ability")
            }

            session.pop("class")
            session.pop("race")
            session.pop("details")
            session.pop("ability")

            mongo.db.characters.insert_one(character)
            flash("Character Successully Created")
            return redirect(url_for("my_characters"))

    classes = mongo.db.classes.find()
    races = mongo.db.races.find()
    backgrounds = mongo.db.backgrounds.find()

    return render_template("new_character.html",
        classes=classes, races=races, backgrounds=backgrounds)


@app.route("/my_characters")
def my_characters():
    characters = mongo.db.characters.find()
    return render_template("my_characters.html", characters=characters)


@app.route("/edit_character/<character_id>", methods=["GET", "POST"])
def edit_character(character_id):
    if request.method == "POST":

        if "class" in request.form:

            index = request.form.get("class")

            session["class_edit"] = {
                "class_name": request.form.get("class_name_" + index),
                "class_hit_die": request.form.get("class_hit_die_" + index),
                "class_skill_prof": request.form.get(
                    "class_skill_prof_" + index)
            }

        if "race" in request.form:

            index = request.form.get("race")

            session["race_edit"] = {
                "race_name": request.form.get("race_name_" + index),
                "race_size": request.form.get("race_size_" + index),
                "race_speed": request.form.get("race_speed_" + index),
                "race_languages": request.form.get("race_languages_" + index)
            }

        if "background" in request.form:

            index = request.form.get("background")

            session["background_edit"] = {
                "background_name": request.form.get(
                    "background_name_" + index),
                "background_languages": request.form.get(
                    "background_languages_" + index),
                "background_skill_prof": request.form.get(
                    "background_skill_prof_" + index),
                "background_equipment": request.form.get(
                    "background_equipment_" + index)
            }

        if "ability_scores" in request.form:
            session["ability_edit"] = {
                "strength": request.form.get("strength"),
                "dexterity": request.form.get("dexterity"),
                "constitution": request.form.get("constitution"),
                "intelligence": request.form.get("intelligence"),
                "wisdom": request.form.get("wisdom"),
                "charisma": request.form.get("charisma"),
            }

        if "submit" in request.form:

            #possibly use a loop odds = key, evens = variables?
            # submit = mongo.db.characters.find_one(
            #     {"_id": ObjectId(character_id)})

            # if session["class_edit"]:
            #     submit.update(session.get("class_edit"))
            # elif session["race_edit"]:
            #     submit.update(session.get("race_edit"))
            # elif session["background_edit"]:
            #     submit.update(session.get("background_edit"))
            # elif session["ability_edit"]:
            #     submit.update(session.get("ability_edit"))

            session.pop("class_edit")
            session.pop("race_edit")
            session.pop("background_edit")
            session.pop("ability_edit")

            mongo.db.characters.update({"_id": ObjectId(character_id)}, submit)
            flash("Character Successully Updated")

    character = mongo.db.characters.find_one(
        {"_id": ObjectId(character_id)})

    characters = mongo.db.characters.find()
    classes = mongo.db.classes.find()
    races = mongo.db.races.find()
    backgrounds = mongo.db.backgrounds.find()

    return render_template("edit_character.html",
        character=character, characters=characters,
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