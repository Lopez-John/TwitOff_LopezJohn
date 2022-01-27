from .models import User
import numpy as np
from sklearn.linear_model import LogisticRegression
from .twitter import vectorize_tweet

def predict_user(user0_username, user1_username, hypto_tweet_text):
    '''
    Determine and returns which user is more likely to say a give tweet
    '''
    # Query for the two users so that we can get their word embeddings
    user0 = User.query.filter(User.username == user0_username).one()
    user1 = User.query.filter(User.username == user1_username).one()

    # Get the word embeddings of the tweets of both users 0 and 1
    user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    user1_vects = np.array([tweet.vect for tweet in user1.tweets])

    #Combine the two user's word embeddings into one big *2D* numpy array
    # This is essentially our X matrix for training out logistic regression
    vects = np.vstack([user0_vects, user1_vects])
    
    # Create a np array to represent the y vector 
    # Indicate which user was the author of given word embedding
    labels = np.concatenate([np.zeros(len(user0.tweets)),
                            np.ones(len(user1.tweets))])

    # import and train out logistic regression
    log_reg = LogisticRegression()

    # train out logistic regression
    log_reg.fit(vects, labels)

    # get the word embeddings for our hype_tweet_text
    hypo_tweet_text = vectorize_tweet(hypo_tweet_text)

    # Generate a prediction
    prediction = log_reg.predict([hypto_tweet_text])

    return prediction[0]