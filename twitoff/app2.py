'''Create a Flask app for
    -displaying tweets
    -reseting the database of tweets
    -testing database'''

from flask import Flask, render_template
from .models2 import DB, User, Tweet


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweet_db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route("/")
    def home_page():
        users = User.query.all()
        print(users)
        return render_template(
                            'base.html',
                            title='Home',
                            users=users
                            )

    @app.route('/populate')
    def populate():

        DB.drop_all()
        DB.create_all()

        ds_lad = User(id=1, username='DS_Lad')
        joe_byron = User(id=2, username='Joe Byron')
        tweet1 = Tweet(
                    id=1,
                    text='I love Data Science',
                    user=ds_lad)
        tweet2 = Tweet(
                    id=2,
                    text="The White House doesn't seem that white",
                    user=joe_byron)
        tweet3 = Tweet(
                        id=3,
                        text='Data Engineering is something different',
                        user=ds_lad)
        tweet4 = Tweet(
                    id=4,
                    text='Mitch McConnell is a giant turle, facts',
                    user=joe_byron)
        tweet5 = Tweet(
                    id=5,
                    text='Government needs more data to do stuff',
                    user=ds_lad)
        tweet6 = Tweet(
                    id=6,
                    text='Business needs makes, like the building and stuff',
                    user=joe_byron)

        DB.session.add(ds_lad)
        DB.session.add(joe_byron)
        DB.session.add(tweet1)
        DB.session.add(tweet2)
        DB.session.add(ds_lad)
        DB.session.add(joe_byron)
        DB.session.add(tweet3)
        DB.session.add(tweet4)
        DB.session.add(tweet5)
        DB.session.add(tweet6)
        DB.session.commit()
        return render_template(
                                'base.html',
                                title='Populate'
                                )

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template(
                                'base.html',
                                title='Reset Database'
                                )

    return app
