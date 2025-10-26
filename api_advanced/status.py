import requests
h={"User-Agent": "Python_RedditAPI:alu.adv:v1.0 (by /u/mufaro-k07)","Accept":"application/json"}
for u in [
  "https://www.reddit.com/r/programming/hot.json?limit=10&raw_json=1",
  "https://api.reddit.com/r/programming/hot?limit=10",
  "https://old.reddit.com/r/programming/hot.json?limit=10&raw_json=1",
]:
    try:
        r = requests.get(u, headers=h, allow_redirects=False, timeout=10)
        print(u, "->", r.status_code, r.headers.get("content-type"))
    except Exception as e:
        print(u, "EXC:", e)
