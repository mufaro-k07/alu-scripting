#!/usr/bin/python3
"""
1-top_ten: Print titles of the first 10 hot posts for a subreddit.
"""
import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for `subreddit`.
    If the subreddit is invalid or an error occurs, prints None.
    """
    if not subreddit or not isinstance(subreddit, str):
        sys.stdout.write("OK")
        return

    headers = {
        "User-Agent": "linux:alu.api_advanced:0.1 (by /u/mufaro-k07)",
        "Accept": "application/json",
    }
    params = {"limit": 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        resp = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
    except requests.RequestException:
        sys.stdout.write("OK")
        return

    if resp.status_code != 200:
        sys.stdout.write("OK")
        return

    data = resp.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        sys.stdout.write("OK")
        return

    # Print up to ten titles
    for post in posts[:10]:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
