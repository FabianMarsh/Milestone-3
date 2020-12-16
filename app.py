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


# Default app route
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Checks which cookies the user has put in session and deletes them
@app.route("/cancel")
def cancel():

    if "class" in session:
        session.pop("class")

    if "race" in session:
        session.pop("race")

    if "background" in session:
        session.pop("background")

    if "details" in session:
        session.pop("details")

    if "ability" in session:
        session.pop("ability")

    return redirect(url_for("profile", username=session['user']))


# Gets stat from request.form.get and converts to 5th edition modifier
@app.route("/get_modifier")
def get_modifier(stat):
    if type(stat) is str:
        int(stat)

    modifier = (stat - 10) / 2
    modifier = math.floor(modifier)

    return modifier


@app.route("/new_character", methods=["GET", "POST"])
def new_character():

    # if user not in session cookies return user redirect to login
    if "user" in session:

        if request.method == "POST":

            # Checks which form has been filled in
            # and then saves session cookie
            if "class" in request.form:

                # Take class_index from button input,
                # attaches to end of input name
                # This was the solution to the form
                # taking first occurance of the name
                # The class index is stored within the database and
                # attached to the name when going through the for loop
                index = request.form.get("class")

                class_hit_die_int = request.form.get(
                    "class_hit_die_" + index).split("d")

                # Get class values
                session["class"] = {
                    "class_name": request.form.get("class_name_" + index),
                    "class_hit_die": request.form.get(
                        "class_hit_die_" + index),
                    "class_hit_die_int": int(class_hit_die_int[1]),
                    "class_total_hit_dice": 1,
                    "temporary_hit_points": 0,
                    "class_saving_throws": request.form.get(
                        "class_saving_throws_" + index),
                    "class_num_skills": int(request.form.get(
                        "class_num_skills_" + index)),
                    "proficiency_bonus": int(request.form.get(
                        "proficiency_bonus")),
                    "character_experience": 0
                }

                # Not all classes have a tool prof field
                # So checks if the class has one and updates cookie
                # this is to see if a tool select needs to be
                # generated on the character details tab
                if "class_tool_prof_" + index in request.form:
                    session["class"].update({
                        "class_tool_prof": request.form.get(
                            "class_tool_prof_" + index)})

                # Check to see if class has class_num_artisans field
                # This is to see how many selects need generating later
                if "class_num_artisans_" + index in request.form:
                    session["class"].update({
                        "class_num_artisans": int(request.form.get(
                            "class_num_artisans_" + index))})
                else:
                    session["class"].update({
                        "class_num_artisans": 0})

                # Check to see if class has class_num_instruments field
                # This is to see how many selects need generating later
                if "class_num_instruments_" + index in request.form:
                    session["class"].update({
                        "class_num_instruments": int(request.form.get(
                            "class_num_instruments_" + index))})
                else:
                    session["class"].update({
                        "class_num_instruments": 0})

                # The class skills are saved in a separate cookie
                # To make generating skill selector simpler
                session["skills"] = [
                    request.form.get("class_skill_prof_" + index)
                ]

            if "race" in request.form:

                # Take race_index from button input,
                # attaches to end of input name
                # This was the solution to the form
                # taking first occurance of the name
                # The race index is stored within the database and
                # attached to the name when going through the for loop
                index = request.form.get("race")

                # Get race values
                session["race"] = {
                    "race_name": request.form.get("race_name_" + index),
                    "race_size": request.form.get("race_size_" + index),
                    "race_speed_num": int(request.form.get(
                        "race_speed_num_" + index)),
                    "race_languages": request.form.get(
                        "race_languages_" + index),
                    "race_language": request.form.get(
                        "race_language_" + index),
                    "race_feature_num": int(request.form.get(
                        "race_feature_num_" + index)),
                    "race_features": " "
                }

                # Not all races have the same amount of features
                # So the amount of features is saved as a value
                # so they can all be saved within the cookie
                for i in range(0, session["race"]["race_feature_num"]):

                    session["race"]["race_features"] += request.form.get(
                        "race_features_" + index + "_" + str(i)) + " "

            if "background" in request.form:

                # Take background_index from button input,
                # attaches to end of input name
                # This was the solution to the form
                # taking first occurance of the name
                # The background index is stored within the database and
                # attached to the name when going through the for loop
                index = request.form.get("background")

                background_feature = request.form.get(
                    "background_feature_name_" + index
                    ) + " " + request.form.get(
                        "background_feature_description_" + index)

                # Gets background values
                session["background"] = {
                    "background_name": request.form.get(
                        "background_name_" + index),
                    "background_skill_prof": request.form.get(
                        "background_skill_prof_" + index),
                    "background_equipment": request.form.get(
                        "background_equipment_" + index),
                    "background_num_languages": int(request.form.get(
                        "background_num_languages_" + index)),
                    "character_copper": 0,
                    "character_silver": 0,
                    "character_electrum": 0,
                    "character_gold": int(request.form.get(
                        "background_gold_" + index)),
                    "character_platinum": 0,
                    "background_feature": background_feature
                    }

                # Not all backgrounds have a tool prof field
                # So checks if the background has one and updates cookie
                # this is to see if a tool select needs to be
                # generated on the character details tab
                if "background_tool_prof_" + index in request.form:
                    session["background"].update({
                        "background_tool_prof": request.form.get(
                            "background_tool_prof_" + index)})

                # Check to see if background has background_num_artisans field
                # This is to see how many selects need generating later
                if "background_num_artisans_" + index in request.form:
                    session["background"].update({
                        "background_num_artisans": int(request.form.get(
                            "background_num_artisans_" + index))})
                else:
                    session["background"].update({
                        "background_num_artisans": 0})

                # Check to see if background has background_num_instruments field
                # This is to see how many selects need generating later
                if "background_num_instruments_" + index in request.form:
                    session["background"].update({
                        "background_num_instruments": int(request.form.get(
                            "background_num_instruments_" + index))})
                else:
                    session["background"].update({
                        "background_num_instruments": 0})

            if "details" in request.form:

                # Get details values
                session["details"] = {
                    "character_name": request.form.get("character_name"),
                    "character_description": request.form.get(
                        "character_description"),
                    "character_alignment": request.form.get(
                        "character_alignment"),
                    "chosen_skills": "",
                    "chosen_languages": "",
                    "player_name": session["user"],
                    "personality_traits": request.form.get(
                        "personality_traits"),
                    "ideals": request.form.get("ideals"),
                    "bonds": request.form.get("bonds"),
                    "flaws": request.form.get("flaws"),
                }

                session["details"].update({
                    "other_languages_proficiencies": " "})

                # Checks if both the class and background cookies exists
                if "class" in session and "background" in session:

                    if "class_tool_prof" in session["class"]:
                        
                        # Combines all selected tools into a single variable
                        for i in range(0, session["class"][
                            "class_num_artisans"] + session[
                                "background"]["background_num_artisans"]):

                            session["details"][
                                "other_languages_proficiencies"
                                ] += request.form.get(
                                    "tool_select_" + str(i)) + ", "

                        # Checks to which single tool is contained with the characters
                        # background or class profiencies. Single tool refers to a tool
                        # not stored in an array
                        if "Disguise" in session["class"]["class_tool_prof"]:

                            session["details"][
                                "other_languages_proficiencies"
                                ] += "Disguise Kit, "

                        if "Forgery" in session["class"]["class_tool_prof"]:

                            session["details"][
                                "other_languages_proficiencies"
                                ] += "Forgery Kit, "

                        if "Herbalism" in session["class"]["class_tool_prof"]:

                            session["details"][
                                "other_languages_proficiencies"
                                ] += "Herbalism Kit, "

                        if "Navigator" in session["class"]["class_tool_prof"]:

                            session["details"][
                                "other_languages_proficiencies"
                                    ] += "Navigator's Tools, "

                        if "Poisoner" in session["class"]["class_tool_prof"]:

                            session["details"][
                                "other_languages_proficiencies"
                                ] += "Poisoner's Kit, "

                        if "Thieves" in session["class"][
                                "class_tool_prof"]:

                            session["details"][
                                "other_languages_proficiencies"
                                ] += "Thieves' Tools, "

                        # Stores instruments in the combined variable of other_languages_profiencies
                        if "instrument" in session["class"][
                                "class_tool_prof"]:

                            for i in range(0, session["class"][
                                    "class_num_instruments"]):

                                session["details"][
                                    "other_languages_proficiencies"
                                        ] += request.form.get(
                                        "instrument_select_" + str(i)) + ", "

                        if "gaming" in session["class"][
                                "class_tool_prof"]:

                            session["details"][
                                "other_languages_proficiencies"
                                ] += request.form.get(
                                    "gaming_select")

                if "background_tool_prof" in session[
                        "background"]:

                    # Checks to which single tool is contained with the characters
                    # background or class profiencies. Single tool refers to a tool
                    # not stored in an array
                    if "Disguise" in session["background"][
                            "background_tool_prof"]:

                        session["details"][
                            "other_languages_proficiencies"
                                ] += "Disguise Kit, "

                    if "Forgery" in session["background"][
                            "background_tool_prof"]:

                        session["details"][
                                "other_languages_proficiencies"
                                ] += "Forgery Kit, "

                    if "Herbalism" in session[
                            "background"]["background_tool_prof"]:

                        session["details"][
                            "other_languages_proficiencies"
                                ] += "Herbalism Kit, "

                    if "Navigator" in session["background"][
                            "background_tool_prof"]:

                        session["details"][
                            "other_languages_proficiencies"
                                ] += "Navigator's Tools "

                    if "Thieves" in session["background"][
                            "background_tool_prof"]:

                        session["details"][
                            "other_languages_proficiencies"
                                ] += "Thieves' Tools "

                    # Stores instruments in the combined variable of other_languages_profiencies
                    if "instrument" in session[
                            "background"]["background_tool_prof"]:

                        for i in range(0, session["background"][
                                "background_num_instruments"]):

                            session["details"][
                                "other_languages_proficiencies"
                                    ] += request.form.get(
                                        "instrument_select_" + str(i)) + ", "

                    # Stores gaming sets in the combined variable of other_languages_profiencies
                    if "gaming" in session["background"][
                            "background_tool_prof"]:

                        session["details"][
                            "other_languages_proficiencies"
                            ] += request.form.get("gaming_select")

                if "class" in session:
                    
                    # Get skills from skill selects
                    for i in range(0, session["class"]["class_num_skills"]):
                        session["details"][
                            "chosen_skills"] += request.form.get(
                                "skill_select_" + str(i)) + ", "
                # Gets background languaes and stores within the combined variable
                session["details"][
                        "other_languages_proficiencies"] += session[
                            "race"]["race_language"]

                if session["background"]["background_num_languages"] > 0:

                    # Get selected background languages and puts in stored variable
                    for i in range(0, session["background"][
                            "background_num_languages"]):

                        session["details"][
                            "other_languages_proficiencies"
                                    ] += request.form.get(
                                        "language_select_" + str(i)) + ", "

            if "ability_scores" in request.form:
                # Gets ability values
                # Whole stat is pushed to the get_modifier function
                # All values are forced into integers as cookies have a 
                # Tendency to store everything as a string
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
                        int(request.form.get("wisdom"))),
                    "charisma": int(request.form.get("charisma")),
                    "charisma_modifier": get_modifier(
                        int(request.form.get("charisma"))),
                    # Calculate intiative bonus and armor class
                    "intiative_bonus": get_modifier(
                        int(request.form.get("dexterity"))),
                    "armor_class": get_modifier(
                        int(request.form.get("dexterity"))) + 10,
                }

                # Calculate passive perception
                # based on whether character has proficiency or not
                if "Perception" in session["details"]["chosen_skills"]:
                    passive_perception = 10 + session[
                        "ability"]["wisdom_modifier"] + session[
                            "class"]["proficiency_bonus"]
                else:
                    passive_perception = 10 + session[
                        "ability"]["wisdom_modifier"]

                session["details"].update({
                    "passive_perception": passive_perception})

                if "class" in session:

                    # Calculates hit_point_maximum
                    hit_point_maximum = session["class"][
                        "class_hit_die_int"] + session[
                            "ability"]["constitution_modifier"]

                    session["class"].update({
                        "hit_point_maximum": hit_point_maximum,
                        "current_hit_points": hit_point_maximum})

                if "background" in session:
                    
                    # Background equipment stored in details cookies
                    session["details"].update({"equipment": session[
                        "background"]["background_equipment"]})

                    session["details"].update({"feature_traits": session[
                        "background"][
                            "background_feature"] + " " + session[
                                "race"]["race_features"]})

            if "submit" in request.form:
                # checks to see if all necessary cookies exists
                # if not informs the user
                if "class" not in session:
                    flash("You haven't picked a class!")
                    return redirect(url_for("new_character"))
                elif "race" not in session:
                    flash("You haven't picked a race!")
                    return redirect(url_for("new_character"))
                elif "background" not in session:
                    flash("You haven't picked a background!")
                    return redirect(url_for("new_character"))
                elif "details" not in session:
                    flash("You haven't filled in your character's details!")
                    return redirect(url_for("new_character"))
                elif "ability" not in session:
                    flash("You haven't picked your ability scores!")
                    return redirect(url_for("new_character"))

                character = {
                    **session.get("class"),
                    **session.get("race"),
                    **session.get("background"),
                    **session.get("details"),
                    **session.get("ability")
                 }

                # Discards all cookies so process can start anew
                session.pop("class")
                session.pop("race")
                session.pop("details")
                session.pop("background")
                session.pop("ability")
                session.pop("skills")

                mongo.db.characters.insert_one(character)
                flash("Character Successully Created")
                return redirect(url_for("profile", username=session['user']))

        classes = mongo.db.classes.find()
        races = mongo.db.races.find()
        backgrounds = mongo.db.backgrounds.find()
        skills = list(mongo.db.skills.find())
        languages = list(mongo.db.languages.find())
        tools = list(mongo.db.tools.find())
        alignments = list(mongo.db.alignments.find())

        return render_template("new_character.html", classes=classes,
            races=races, backgrounds=backgrounds, skills=skills,
                languages=languages, tools=tools,
                    alignments=alignments)

    return redirect(url_for("login"))


@app.route("/edit_character/<character_id>", methods=["GET", "POST"])
def edit_character(character_id):

    if "user" in session:
        saving_throws = mongo.db.saving_throws.find()
        skills = mongo.db.skills.find()

        if request.method == "POST":

            class_saving_throws = " "
            chosen_skills = " "

            # Checks to if which saving throws the character has profiency in
            for saving_throw in saving_throws:
                check = request.form.get(saving_throw["saving_throw_name"])
                if check == "on":
                    class_saving_throws = class_saving_throws + saving_throw[
                        "saving_throw_name"] + " "
            # Checks to if which skills the character has profiency in
            for skill in skills:
                check = request.form.get(skill["skill_name"])
                if check == "on":
                    chosen_skills = chosen_skills + skill["skill_name"] + " "

            # Removes + from intiative and profiency bonus
            intiative_bonus = request.form.get("intiative_bonus")
            if "+" in intiative_bonus:
                intiative_bonus = intiative_bonus.split("+")
                intiative_bonus = intiative_bonus[1]

            proficiency_bonus = request.form.get("proficiency_bonus")
            if "+" in proficiency_bonus:
                proficiency_bonus = proficiency_bonus.split("+")
                proficiency_bonus = proficiency_bonus[1]

            # Takes all fields from edit form
            submit = {
                "character_name": request.form.get("character_name"),
                "class_name": request.form.get("class_name"),
                "background_name": request.form.get("background_name"),
                "player_name": request.form.get("player_name"),
                "race_name": request.form.get("race_name"),
                "character_alignment": request.form.get("character_alignment"),
                "character_experience": int(request.form.get(
                    "character_experience")),
                "proficiency_bonus": int(proficiency_bonus),
                "strength": int(request.form.get("strength")),
                "strength_modifier": get_modifier(int(request.form.get(
                    "strength"))),
                "dexterity": int(request.form.get("dexterity")),
                "dexterity_modifier": get_modifier(int(request.form.get(
                    "dexterity"))),
                "constitution": int(request.form.get("constitution")),
                "constitution_modifier": get_modifier(int(request.form.get(
                    "constitution"))),
                "intelligence": int(request.form.get("intelligence")),
                "intelligence_modifier": get_modifier(int(request.form.get(
                    "intelligence"))),
                "wisdom": int(request.form.get("wisdom")),
                "wisdom_modifier": get_modifier(int(request.form.get(
                    "wisdom"))),
                "charisma": int(request.form.get("charisma")),
                "charisma_modifier": get_modifier(int(request.form.get(
                    "charisma"))),
                "class_saving_throws": class_saving_throws,
                "chosen_skills": chosen_skills,
                "passive_perception": int(request.form.get(
                    "passive_perception")),
                "other_languages_proficiencies": request.form.get(
                    "other_languages_proficiencies"),
                "armor_class": int(request.form.get("armor_class")),
                "intiative_bonus": int(intiative_bonus),
                "race_speed_num": request.form.get("race_speed_num"),
                "hit_point_maximum": int(request.form.get(
                    "hit_point_maximum")),
                "current_hit_points": int(request.form.get(
                    "current_hit_points")),
                "temporary_hit_points": int(request.form.get(
                    "temporary_hit_points")),
                "class_total_hit_dice": int(request.form.get(
                    "class_total_hit_dice")),
                "class_hit_die": request.form.get("class_hit_die"),
                "attack_name_1": request.form.get("attack_name_1"),
                "attack_bonus_1": request.form.get("attack_bonus_1"),
                "attack_damage_1": request.form.get("attack_damage_1"),
                "attack_name_2": request.form.get("attack_name_2"),
                "attack_bonus_2": request.form.get("attack_bonus_2"),
                "attack_damage_2": request.form.get("attack_damage_2"),
                "attack_name_3": request.form.get("attack_name_3"),
                "attack_bonus_3": request.form.get("attack_bonus_3"),
                "attack_damage_3": request.form.get("attack_damage_3"),
                "attacks_spellcasting": request.form.get(
                    "attacks_spellcasting"),
                "character_copper": int(request.form.get("character_copper")),
                "character_silver": int(request.form.get("character_silver")),
                "character_electrum": int(request.form.get(
                    "character_electrum")),
                "character_gold": int(request.form.get("character_gold")),
                "character_platinum": int(request.form.get(
                    "character_platinum")),
                "equipment": request.form.get("equipment"),
                "personality_traits": request.form.get("personality_traits"),
                "ideals": request.form.get("ideals"),
                "bonds": request.form.get("bonds"),
                "flaws": request.form.get("flaws"),
                "feature_traits": request.form.get("feature_traits"),
                "character_description": request.form.get(
                    "character_description")
            }

            mongo.db.characters.update({"_id": ObjectId(character_id)}, submit)
            flash("Character Successully Updated")
            return redirect(url_for("profile", username=session['user']))

        # skills and saving throws are defined above
        # as the POST function also uses them

        character = mongo.db.characters.find_one(
            {"_id": ObjectId(character_id)})

        return render_template("edit_character.html", character=character,
            saving_throws=saving_throws, skills=skills)

    return redirect(url_for("login"))


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


@app.route("/delete_character/<character_id>")
def delete_character(character_id):
    mongo.db.characters.remove({"_id": ObjectId(character_id)})
    flash("Character Successfully Removed")
    return redirect(url_for("profile", username=session['user']))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab session user's username for the db
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        characters = mongo.db.characters.find()
        return render_template("profile.html", username=username,
            characters=characters)

    return redirect(url_for("login"))


@app.route("/character_gallery")
def character_gallery():

    characters = mongo.db.characters.find()
    return render_template("character_gallery.html", characters=characters)


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect("login")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
