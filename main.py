"""
This is the main file for the Reddit bot.
To get the posts with specific keywords, we use the PRAW library.
"""

import praw
import json


def get_reddit_instance(id, secret, agent, username, password):
    """
    This function returns a Reddit instance.
    """
    client_id = id if id else "D_2aShbm6PLts9WyjUU4Cg"
    client_secret = secret if secret else "nmkTYmUyxowHaufxAcvSp7aF-schTA"
    user_agent = agent if agent else "TempVersion:0.1"
    username = username if username else "maiqjiang2"
    password = password if password else json.load(open("masked.json", "r"))

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password
    )
    return reddit


def verify_reddit_instance(reddit):
    """
    This function verifies the Reddit instance.
    """
    print(reddit.user.me())


def get_posts(reddit, keyword, limit=10):
    """
    This function returns a list of posts with the keyword.
    """
    posts = []
    for submission in reddit.subreddit("all").search(keyword, limit=limit):
        posts.append(submission)
    return posts
