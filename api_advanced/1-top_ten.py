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
        "Accept": "application/json",
    }
    params = {"limit": 10}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        resp = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
        if resp.status_code != 200:
            print("None")
            return
        data = resp.json()
    except Exception:
        print("None")
        return

    posts = data.get("data", {}).get("children", [])
    if not posts:
        print("None")
        return

    for post in posts[:10]:
        title = post.get("data", {}).get("title")
        if title is None:
            print("None")
            return
        print(title)
