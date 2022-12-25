import os

DATA_FILE = "posts.json"
PICTURE_FOLDER = os.path.join("uploads", "images")
VALID_EXT = ["jpeg", "png", "jpg"]
LOG_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(LOG_DIR, "basic.log")