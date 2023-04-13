from datetime import datetime
from flask import current_app, render_template

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


def animals_page():
    db = current_app.config["db"]
    animals = db.get_animals()
    return render_template("animals.html", animals=sorted(animals))


def animal_page(animal_key):
    db = current_app.config["db"]
    animal = db.get_animal(animal_key)
    return render_template("animal.html", animal=animal)
