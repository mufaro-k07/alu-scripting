#!/usr/bin/python3
"""
2-recurse: Return a list of titles for all hot posts in a subreddit, recursively.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively collects titles of all hot posts for `subreddit`.

    Args:
        subreddit (str): Subreddit name (without leading 'r/').
        hot_list (list): Accumulator for titles (created on first call).
        after (str): Reddit pagination token for the next page.

    Returns:
        list or None: List of titles, or None if invalid subreddit or no results.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    if hot_list is None:
        hot_list = []

    headers = {
        "User-Agent": "linux:alu.api_advanced:0.1 (by /u/mufaro-k07)",
        "Accept": "application/json",
    }

    params = {"limit": 100}
    if after:
        params["after"] = after

    url1 = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url2 = "https://api.reddit.com/r/{}/hot".format(subreddit)

    try:
        resp = requests.get(
            url1, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
        if resp.status_code == 200:
            data = resp.json()
        else:
            resp2 = requests.get(
                url2, headers=headers, params=params,
                allow_redirects=False, timeout=10
            )
            if resp2.status_code != 200:
                return None if not hot_list else hot_list
            data = resp2.json()
    except (requests.RequestException, ValueError):
        return None if not hot_list else hot_list

    children = data.get("data", {}).get("children", [])
    for child in children:
        title = child.get("data", {}).get("title")
        if title is not None:
            hot_list.append(title)

    next_after = data.get("data", {}).get("after")
    if next_after:
        return recurse(subreddit, hot_list, next_after)

    # No more pages. If we collected nothing, return None as required.
    return hot_list if hot_list else None
