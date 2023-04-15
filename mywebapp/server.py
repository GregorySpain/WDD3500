from flask import Flask
import views
from database import Database
from animal import Animal


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/animals", view_func=views.animals_page, methods=["GET", "POST"])
    app.add_url_rule("/animals/<int:animal_key>/edit", view_func=views.edit_animal_page, methods=["GET", "POST"])
    app.add_url_rule("/animals/<int:animal_key>", view_func=views.animal_page)
    app.add_url_rule("/new_animal", view_func=views.add_animal_page, methods=["GET", "POST"])
    app.register_error_handler(404, views.page_not_found)

    db = Database()
    app.config["db"] = db
    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="127.0.0.1", port=port)
    app.config.get


