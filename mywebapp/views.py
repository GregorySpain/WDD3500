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
    # (3.5) This was a little tricky, but once I got the overall 404 set up, it clicked that I would
    # have to do something in here, because this method accepts any value. So I handled it with
    # a basic conditional.
    if animal is None:
        return page_not_found(404)
    return render_template("animal.html", animal=animal)


def page_not_found(error):
    return render_template("404.html"), 404
