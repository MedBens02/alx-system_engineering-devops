#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    '''Top 10'''
    resp = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/125.0.0.0 Safari/537.36"
        },
        params={"limit": 11},  # Fetch one more than needed
        allow_redirects=False
    )

    if resp.status_code == 200:
        results = resp.json().get("data")
        children = results.get("children")
        if len(children) > 1 and children[0].get("data").get("stickied"):
            children = children[1:]  # Exclude the sticky post if it's present
        [print(c.get("data").get("title")) for c in children[:10]]  # Print only the first 10
    else:
        print("None") 
