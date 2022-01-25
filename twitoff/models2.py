'''Holds DB Schema for users and tweets'''
from flask_sqlalchemy import SQLAlchemy

# Cretes a DB object
DB = SQLAlchemy()

# Creates a User table with a specific schema
class User(DB.Model):
    # Two columns inside the User table
    id = DB.Column(
                    DB.BigInteger,
                    primary_key=True,
                    nullable=False
                    )
    username = DB.Column(
                        DB.String,
                        nullable=False
                        )

#Creates a Tweet table
class Tweet(DB.Model):
    # Four columns inside the Tweet table
    id = DB.Column(
                    DB.BigInteger,
                    primary_key=True,
                    nullable=False
                    )
    text = DB.Column(
                    DB.Unicode(300),
                    nullable=False
                    )
    # Sets ups the Secondary/Foreign key
    user_id = DB.Column(
                        DB.BigInteger,
                        DB.ForeignKey('user.id'),
                        nullable=False
                        )
    # Sets up the relationship between the Tweets and the users
    user = DB.relationship(
                            "User",
                            backref=DB.backref('tweets'),
                            lazy=True
                            )
