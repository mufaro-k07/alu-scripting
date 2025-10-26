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
        print(None)
        return

    headers = {
        "User-Agent": "alu.api_advanced:0.1 (by mufaro-k07)"
    }
    params = {"limit": 10}

    # Primary: www.reddit.com
    url1 = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url2 = "https://api.reddit.com/r/{}/hot".format(subreddit)

    try:
        r = requests.get(url1, headers=headers, params=params,
                         allow_redirects=False, timeout=10)
        if r.status_code == 200:
            data = r.json()
        else:
            # Try the API domain as a fallback
            r2 = requests.get(url2, headers=headers, params=params,
                              allow_redirects=False, timeout=10)
            if r2.status_code != 200:
                print(None)
                return
            data = r2.json()
    except (requests.RequestException, ValueError):
        print(None)
        return

    posts = data.get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts[:10]:
        title = post.get("data", {}).get("title")
        if title is None:
            print(None)
            return
        print(title)
