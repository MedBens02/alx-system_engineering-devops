#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    '''Function that queries the Reddit API'''
    resp = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={
            "User-Agent": "bensm02"
        },
        allow_redirects=False
    )
    if resp.status_code == 200:
        results = resp.json().get("data")
        return results.get("subscribers")
    else:
        return 0
