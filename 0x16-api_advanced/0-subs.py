#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    '''Function that queries the Reddit API'''
    APIurl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers={"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bensm02)"}

    response = requests.get(APIurl, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0

    data = response.json()
    return data.get("data").get("subscribers")
