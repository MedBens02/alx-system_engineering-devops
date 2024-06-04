#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    '''Function that queries the Reddit API'''
    APIurl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers={"User-Agent": "Custom"}

    try:
        response = requests.get(APIurl, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("data").get("subscribers")
        else:
            return 0
    except requests.RequestException:
        return 0
