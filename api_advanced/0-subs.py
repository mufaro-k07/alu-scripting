#!/usr/bin/python3
"""
0-subs: Return the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit's API and returns the subscriber count for `subreddit`.
    Returns 0 if the subreddit is invalid or on any error.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api_advanced:0.1 (by mufaro-k07)",
        "Accept": "application/json",
    }

    try:
        resp = requests.get(url, headers=headers, allow_redirects=False)
    except requests.RequestException:
        return 0

    if resp.status_code != 200:
        return 0

    try:
        payload = resp.json()
    except ValueError:
        return 0

    return payload.get("data", {}).get("subscribers", 0)
