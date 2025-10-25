#!/usr/bin/python3
"""
Gets the number of subscribers for the given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
	"""Returns the number of subscribers for a subreddit."""
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
