#!/usr/bin/python3
"""
Contains the function top_ten(subreddit)
that queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    headers = {
        "User-Agent": "alu.api_advanced:0.1 (by mufaro-k07)",
        "Accept": "application/json",
    }
    params = {"limit": 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
