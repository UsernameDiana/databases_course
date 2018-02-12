import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.social_net


def get_total_user_amount():
    print (len(db.tweets.distinct('user')))


def get_users_who_mentions_others():
    print ('???')


def get_most_mentioned_users():
    pipeline = [
        {'$addFields': {'words': {'$split': ['$text', ' ']}}},  # split text
        {'$unwind': "$words"},  # reconstruct an array of words
        {'$match': {'words': {'$regex': "@\w+", '$options': 'm'}}}, # match the @ from the words list
        {'$group': {'_id': "$words", 'total': {'$sum': 1}}},
        {'$sort': {'total': -1}},  # sort the total
        {'$limit': 5},
    ]
    tweets = db.tweets.aggregate(pipeline)
    print (list(tweets))


def get_most_active_users():
    pipeline = [
        {'$group': {'_id': "$user", 'total': {'$sum': 1}}},
        {'$sort': {'total': -1}},
        {'$limit': 10},
    ]
    users = db.tweets.aggregate(pipeline)
    print(list(users))


def get_most_negative_tweets():
    pipeline = [
        {'$match': {'text': {'$regex': "worst$"}}},
        {'$project': {'_id': 0, 'user': 1}},
        {'$limit': 5},
    ]
    users = db.tweets.aggregate(pipeline)
    print (list(users))


def get_most_positive_tweets():
    pipeline = [
        {'$match': {'text': {'$regex': "love$"}}},
        {'$project': {'_id': 0, 'user': 1}},
        {'$limit': 5},
    ]
    users = db.tweets.aggregate(pipeline)
    print (list(users))


# print ('How many Twitter users are in the database?')
# get_total_user_amount()
# print('Top 10 users link the most to other Twitter users?')
# get_users_who_mentions_others()
# print('Top 5 most mentioned Twitter users? ')
# get_most_mentioned_users()
print('Top 10 most active Twitter users are: ')
get_most_active_users()
# print('Top 5 users tweeting word "worst": ')
# get_most_negative_tweets()
# print ('Top 5 users tweeting word "love": ')
# get_most_positive_tweets()
