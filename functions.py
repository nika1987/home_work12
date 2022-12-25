import logging
import json
from constants import DATA_FILE, VALID_EXT, LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, encoding="utf=8")
def posts_from_json(path):
    """
     функция возвращает все запрошенные посты
    """
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        logging.error(f"Файл {path} не найден")
        return []
    except json.JSONDecoder:
        print("Не удалось декодировать json file")
        logging.error("Не удалось декодировать json file")
        return []

def find_posts(find_word):
    """
    функция возвращает один пост по веб адресу

    """
    found_post = []
    for post in posts_from_json(DATA_FILE):
        if find_word in post["content"]:
            found_post.append(post)
    return found_post

def add_new_post(file_name,content):
    """
    функция принимает добавляет новый пост в json

    """
    posts = posts_from_json(DATA_FILE)
    new_post = {
        "pic":"/uploads/" + file_name,
        "content": content
    }

    posts.append(new_post)
    save_posts(DATA_FILE, posts)
    return new_post

def save_posts(file_name, posts):
    """
    функция записывает список постов в файл

    """
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False)

    except FileNotFoundError:
        print(f"Файл {file_name} не найден")
        logging.error(f"Файл {file_name} не найден")


def is_file_valid(file_name):
    """
    функция проверяет что файл является допустимым
    """
    expansion = file_name.split(".")[-1]
    return expansion in VALID_EXT
