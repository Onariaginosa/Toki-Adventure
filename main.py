 #this is a test
import webapp2
from random import shuffle
import os
import jinja2

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_env.get_template("templates/welcome.html")
        self.response.write(welcome_template.render())

class Character(webapp2.RequestHandler):
    def get(self):
        self.response.write("Choose Your character party ppl")

class DogStory(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template("templates/welcome.html")
        self.response.write(template.render())

class PandaStory(webapp2.RequestHandler):
    def get(self):
        self.response.write("Story goes here for Panda")
class CatStory(webapp2.RequestHandler):
    def get(self):
        self.response.write("Story goes here for Cat")


app = webapp2.WSGIApplication([
   ('/', MainPage),
   ('/character',Character),
   ('/dog',DogStory),
   ('/panda',PandaStory),
   ('/cat',CatStory)
], debug=True)
