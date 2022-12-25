from flask import Blueprint, render_template, request
from functions import find_posts
import logging
from constants import LOG_FILE
# импортируем блюпринт
main_blueprint = Blueprint("main_blueprint", __name__)
# создаем экземляр класса (блюпринта)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)


@main_blueprint.route('/')
def index_page():
    return render_template("index.html")


@main_blueprint.route('/search/')
def search_page():
    search_word = request.args.get("s")
    logging.info(f"Поиск {search_word}")
    found_post = find_posts(search_word)

    return render_template("post_list.html", word=search_word, found_post=found_post)
