from datetime import datetime
from flask import current_app, render_template, request, redirect, url_for
from animal import Animal


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


def animals_page():
    db = current_app.config["db"]
    if request.method == "GET":
        animals = db.get_animals()
        return render_template("animals.html", animals=sorted(animals))
    else:
        form_animal_keys = request.form.getlist("animal_keys")
        for form_animal_key in form_animal_keys:
            db.delete_animal(int(form_animal_key))
        return redirect(url_for("animals_page"))


def animal_page(animal_key):
    db = current_app.config["db"]
    animal = db.get_animal(animal_key)
    # (3.5) This was a little tricky, but once I got the overall 404 set up, it clicked that I would
    # have to do something in here, because this method accepts any value. So I handled it with
    # a basic conditional.
    if animal is None:
        return page_not_found(404)
    return render_template("animal.html", animal=animal)


def animal_add_page():
    if request.method == "GET":
        return render_template("edit_animal.html", min_year=1887, max_year=datetime.now().year)
    else:
        form_species = request.form["species"]
        form_year = request.form["year"]
        animal = Animal(form_species, year=int(form_year) if form_year else None)
        db = current_app.config["db"]
        animal_key = db.add_animal(animal)
        return redirect(url_for("animal_page", animal_key=animal_key))


def page_not_found(error):
    return render_template("404.html"), 404
