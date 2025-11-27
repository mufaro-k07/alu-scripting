#!/usr/bin/python3
"""
1-top_ten: Print titles of the first 10 hot posts for a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for `subreddit`.
    If the subreddit is invalid or an error occurs, prints None.
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    headers = {
        "User-Agent": ("Mozilla/5.0 (X11; Linux x86_64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/117.0.0.0 Safari/537.36"),
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        print(None)
        return

    try:
        posts = resp.json().get("data").get("children")
    except Exception:
        print(None)
        return

    for post in posts:
        print(post.get("data").get("title"))
