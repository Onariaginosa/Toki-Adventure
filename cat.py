from models import Character, Born, PB2, PPath, Path, Looper, KPath
from seed_data import seed_data
from random import randrange
import jinja2
import os

post_born_opt = 0


jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)

def kat_born():
    kitty_key = Character.query(Character.species == "Cat").get()
    kitty_born = Born.query(Born.owner == kitty_key.key).get()
    born_opt = randrange(1,4)
    if born_opt == 1:
        return kitty_born.born_1
    elif born_opt == 2:
        return kitty_born.born_2
    elif born_opt == 3:
        return kitty_born.born_3
def kat_post_born():
    global post_born_opt
    kitty_key = Character.query(Character.species == "Cat").get()
    kitty_post_born = PB2.query(PB2.owner == kitty_key.key).get()
    post_born_opt = randrange(1,4)
    if post_born_opt == 1:
        return kitty_post_born.pb_1
    elif post_born_opt == 2:
        return kitty_post_born.pb_2
    elif post_born_opt == 3:
        return kitty_post_born.pb_3

def kitty_loop():
    kitty_key = Character.query(Character.species == "Cat").get()
    kitty_looper = Looper.query(Looper.owner == kitty_key.key).get()
    global post_born_opt
    if post_born_opt == 1:
        return [kitty_looper.loop_1, 1]
    elif post_born_opt == 2:
        return [kitty_looper.loop_2, 2]
    elif post_born_opt == 3:
        return [kitty_looper.loop_3, 3]

# def number():
#     global post_born_opt
#     if post_born_opt == 1 or post_born_opt == 2 or post_born_opt == 3 or == 0:
#         return post_born_opt

def kitty_pathB():
    kitty_key = Character.query(Character.species == "Cat").get()
    kitty_pather = KPath.query(KPath.owner == kitty_key.key).get()
    global post_born_opt
    if post_born_opt == 2:
        return kitty_pather.p_2b
    elif post_born_opt == 3:
        return kitty_pather.p_3b

def kitty_pathA():
    kitty_key = Character.query(Character.species == "Cat").get()
    kitty_pathers = KPath.query(KPath.owner == kitty_key.key).get()
    global post_born_opt
    if post_born_opt == 2:
        return kitty_pathers.p_2a
    elif post_born_opt == 3:
        return kitty_pathers.p_3a
