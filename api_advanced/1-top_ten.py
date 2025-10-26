#!/usr/bin/python3
"""
Prints titles of the first 10 hot posts for a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for `subreddit`.
    If the subreddit is invalid or an error occurs, prints None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    headers = {
        "User-Agent": "alu.api_advanced:0.1 (by mufaro-k07)"
    }
    params = {"limit": 10}

    url1 = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = get(url, headers=headers, params=params, allow_redirects=False)
    results = response.json()

    try:
	my_data = results.get('data').get('children')

	for i in my_data:
	    print(i.get('data').get('title'))

    except Exception:
	print("None")
