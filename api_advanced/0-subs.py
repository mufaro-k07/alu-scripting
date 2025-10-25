#!/usr/bin/python3
"""
Reddit API helper for subscriber counts.

This module exposes a single function, `number_of_subscribers(subreddit)`,
which returns the number of subscribers for a given subreddit (or 0 if the
subreddit is invalid or inaccessible)
"""
import requests


def number_of_subscribers(subreddit):
	"""Returns the number of subscribers for a subreddit.
	
	Args:
		subreddit (str): the subreddit name
	
	Returns:
		int: Subscriber count if available, otherwise 0.
	"""
	# Getting the URL for the Reddit API endpoint
	url = f"https://www.reddit.com/r/{subreddit}/about.json"

	# Createing the User-Agent for Reddit
	headers = {'User-Agent': 'python:api_advanced:v1.0 (by Mufaro)'}

	# Creating the request and not allowing redirects
	response = requests.get(url, headers = headers, allow_redirects=False)

	# Checking the validity the of the response
	if response.status_code == 200:
		data = response.json()

	# If status successful then get subscribers from the subreddit
		subscribers = data['data']['subscribers']
		return subscribers

	# If unsuccessful or the subreddit doesn't exist, then it safely returns 0.
	else:
		return 0
