from flask import Flask, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint
from constants import PICTURE_FOLDER
POST_PATH = "posts.json"


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory(PICTURE_FOLDER, path)



if __name__ == '__main__':
    app.run()
