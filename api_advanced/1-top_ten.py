#!/usr/bin/python3
"""Reddit API helper: print titles of first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is invalid or there are no posts, prints 'None'.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:api_advanced.top_ten:v1.0 (by /u/alx_student)"
    }
    params = {"limit": 10}

    # Do NOT follow redirects – required by the task
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        print("None")
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title is not None:
            print(title)
