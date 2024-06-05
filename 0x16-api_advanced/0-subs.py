#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    '''Function that queries the Reddit API'''
    resp = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bensm02)"},
        allow_redirects=False
    )

    if resp.status_code == 404:
        return 0
    results = resp.json().get("data")
    return results.get("subscribers")
