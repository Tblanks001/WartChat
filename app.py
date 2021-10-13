from flask import Flask, request, jsonify

#This allows you to create an external database that is capable of interacting with Flask
from flask_sqlalchemy import SQLAlchemy   

#This gived us the ability to fetch posts from a schema of the database
from flask_marshmallow import Marshmallow 

import os
from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
#from database import DataBase


# Init app. "__name__ is referencing this file"
app = Flask(__name__)

# Makes sure the server knows exactly where the database file is
basedir = os.path.abspath(os.path.dirname(__file__))

# Tells the Flask application where the database will be stored. In this situation, we are using a sqlite database
# A databse file is created called 'db.sqlite' 
# 'os.path.join(basedir' finds where the databse is located on our computer
# 'db.sqlite' is the name of our database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Created the database, and connects it to the Flask application
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)


# Product Class/Model
# This BlogPost class inherits from our database model
class BlogPost(db.Model):

    #This makes a column in the database to help identify each post. 
    # Because this is the primary key, it is the main distinguisher between blog posts
    id = db.Column(db.Integer, primary_key=True)

    # 'nullable' means that there must be something in this field. 
    # 'db.string(20)' prevents the name field from being more than 20 characters
    name = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # 'default=datetime.utcnow' returns the Coordinated Universale Time(UTC)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    #These are the things we want added to the instance of every post
    def __init__(self, content, name):
        self.content = content
        self.name = name

# Allows you to decide what fields you want to show from every post in the database
class BlogPostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'content', 'date_posted')

# Initializes the BlogPostSchema
# Allows us to fetch a single post
blogpost_schema = BlogPostSchema()

# Allows us to fetch multiple posts
blogposts_schema = BlogPostSchema(many=True)

class BlogActions:
  #App Routes call URLs

  # Create a Post. methods=['POST'] means that you can only use post requests on this webpage
  @app.route('/posts', methods=['POST'])

  #This is the code that runs whenever the url is called
  def posts(): 
    
    # Uses the Flask request library to turn the information we will be placing into the 'content' field into JSON
    # JSON is code that is readable by a server
    post_content = request.json['content']
    post_name = request.json['name']

    # This adds a new row into the database 
    # We only need to give it the content and the name because that is what we initialized
    new_post = BlogPost(content=post_content, name=post_name)

    # Adds to the database
    db.session.add(new_post)

    # Saves the entry we just added to the database
    db.session.commit()
    
    # returns to the client the new post we just added to the database
    # We use 'blogpost_schema' because it is a single post we are adding
    # 'jsonify' gives the server the new_post in JSON format
    return blogpost_schema.jsonify(new_post)


  # Get all Posts
  @app.route('/posts', methods=['GET'])
  def get_posts():
    
    all_posts = BlogPost.query.all()
    result = blogposts_schema.dump(all_posts)
    return jsonify(result)
    

  # Get Single Post
  @app.route('/posts/<id>', methods=['GET'])
  def get_post(id):
    post = BlogPost.query.get(id)
    return blogpost_schema.jsonify(post)

  # Get posts since a specific post was made
  @app.route('/getsince/<id>', methods=['GET'])
  def getSince(id):
    n = int(id)
    p = []
    p.append(n)
    n = n + 1

    while n != len(BlogPost.query.all()) + 1:
      p.append(n)
      n = n + 1

    posts = BlogPost.query.filter(BlogPost.id.in_(p))
    result = blogposts_schema.dump(posts)
    
    return jsonify(result)

  # Get the last n amount of posts
  @app.route('/lastn/<n>', methods = ['GET'])
  def lastn(n):
    posts = BlogPost.query.order_by(BlogPost.id.desc()).limit(n)
    posts =posts[::-1]

    result = blogposts_schema.dump(posts)

    return jsonify(result)



'''
class WindowManager(ScreenManager):
    # Responsible for moving things around on the screen
    pass

class ChatWindow(Screen):
    post = ObjectProperty(None)

kv = Builder.load_file("my.kv")

sm = WindowManager()

screens = [ChatWindow(name="room")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "room"

class MyMainApp(App):
    def build(self):
        return sm
'''
# This makes sure that if we are running this file directly, debug mode is turned on
if __name__ == '__main__':

  #MyMainApp().run()
  app.run(debug=True)