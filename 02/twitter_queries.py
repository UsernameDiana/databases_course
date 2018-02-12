import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.social_net


def get_total_user_amount():
    print (len(db.tweets.distinct('user')))


# def users_who_mentions_most(results_limit=10):
# def most_mentioned_users(results_limit=5):
# def most_active_users(results_limit=10):


def most_negative_tweets():
    pipeline = [
        {'$match': {'text': {'$regex': "worst$"}}},
        {'$project': {'_id': 0, 'user': 1}},
        {'$limit': 5},
    ]
    tweets = db.tweets.aggregate(pipeline)
    print (list(tweets))


def most_positive_tweets():
    pipeline = [
        {'$match': {'text': {'$regex': "love$"}}},
        {'$project': {'_id': 0, 'user': 1}},
        {'$limit': 5},
    ]
    tweets = db.tweets.aggregate(pipeline)
    print (list(tweets))


# print ('How many Twitter users are in the database?')
# get_total_user_amount()
print('Top 5 users tweeting word "worst": ')
most_negative_tweets()
print ('Top 5 users tweeting word "love": ')
most_positive_tweets()
