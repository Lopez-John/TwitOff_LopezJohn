from flask_sqlalchemy import SQLAlchemy

# Create a DB object
DB = SQLAlchemy()

# Create a table with a specific schema
# we will do that by creating a python class

class User(DB.Model):
    # Two columns inside of our user table
    # ID Column schema
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    # username Column schema
    username = DB.Column(DB.String, nullable=False)
    # Tweets list is created by the relationship and backref in the Tweets class
    # tweets = []

class Tweet(DB.Model):

    # ID Column schema
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    # Text Column Schema
    text = DB.Column(DB.Unicode(300), nullable=False)
    # User Column Schema (Secondary / Foreign Key)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    #set up a relationship betwee the tweets and the users
    # This will automatically create the one-many relationship, but also add a new attribute
    # onto the 'User' class called 'tweets' which will be a list of all the user tweets
    user = DB.relationship("User", backref=DB.backref('tweets'), lazy=True)
