from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():

    
    app = Flask(__name__)

    #configuration variable to our app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Connect our database to the app object
    DB.init_app(app)

    @app.route("/")
    def hello_world():
        users = User.query.all()
        print(users)
        return render_template('base.html', title='Home', users=users)

    @app.route('/populate')
    # test my database functionality
    # by inserting some fake data into the DB
    def populate():

        DB.drop_all()
        DB.create_all()
        #make two new users
        ryan = User(id=1, username='ryanallread')
        julian = User(id=2, username='julian')

        # Make two tweets
        tweet1 = Tweet(id=1, text="this is Ryan's tweet", user=ryan)
        tweet2 = Tweet(id=2, text="this is julian's tweet", user=julian)


        #inserting into the DB when working with SQLite directly
        DB.session.add(ryan)
        DB.session.add(julian)
        DB.session.add(tweet1)
        DB.session.add(tweet2)

        DB.session.commit()
        return render_template('base.html', title='Populate')
        # make two tweets and attach the tweets to those users


    @app.route('/reset')
    def reset():
        # Do some database stuff
        # Drop old DB tables
        # Remake new DB tables
        # remove everything from the DB
        DB.drop_all()
        # recreate the user and Tweet tables
        # so that they're ready to be user (inserted_into)
        DB.create_all()
        return render_template('base.html', title='Reset Database')

    return app