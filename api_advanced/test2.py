#!/usr/bin/python3
"""
Local test file to mock Reddit API for 1-top_ten.py
"""
from types import SimpleNamespace
import requests

# --- Mock Reddit API Response ---
def fake_get(url, headers=None, params=None, allow_redirects=False, timeout=10):
    data = {
        "data": {"children": [
            {"data": {"title": "Post A"}},
            {"data": {"title": "Post B"}},
            {"data": {"title": "Post C"}},
        ]}
    }
    return SimpleNamespace(status_code=200, json=lambda: data)

# Temporarily replace requests.get
real_get = requests.get
requests.get = fake_get

# --- Import function from 1-top_ten.py ---
top_ten = __import__('1-top_ten').top_ten

# --- Test call ---
top_ten("programming")

# Restore real requests.get
requests.get = real_get

