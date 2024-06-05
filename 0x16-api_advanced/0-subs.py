#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    '''Function that queries the Reddit API'''
    resp = requests.get(
        "https://www.reddit.com/r/{}/about/.json".format(subreddit),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/125.0.0.0 Safari/537.36"
        },
        allow_redirects=False
    )
    if resp.status_code != 200:
        return 0
    else:
        results = resp.json().get("data")
        return results.get("subscribers")
