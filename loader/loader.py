import logging
import os
from flask import Blueprint, render_template, request
from functions import add_new_post, is_file_valid
from constants import PICTURE_FOLDER, LOG_FILE

loader_blueprint = Blueprint("loader_blueprint", __name__)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, encoding="utf=8")

@loader_blueprint.route("/post/")
def add_post():
    return render_template("post_form.html")

@loader_blueprint.route("/post/", methods=["POST"])
def post_added():
    file = request.files["picture"]
    content = request.form["content"]
    if is_file_valid(file.filename):
        file.save(os.path.join(PICTURE_FOLDER, file.filename))
        new_post = add_new_post(file.filename, content)
        return render_template("post_uploaded.html", new_post=new_post)
    logging.info(f"file {file.filename} является не допустимым")
    return f"Данный формат файла является не допустимым"
