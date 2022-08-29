import os
import requests
import praw
import requests.auth
from datetime import datetime
import shutil
from appscript import app, mactypes
import json

f = open('key.json')

data = json.load(f)

fname = datetime.now().strftime('%H-%M-%S-%m-%d-%Y')
fname = data["fname"] + fname
print(fname)

reddit = praw.Reddit(
    client_id = data["client_id"],
    client_secret = data["client_secret"],
    user_agent = "ChangeMeClient/0.1 by Nice-Cut-5030"
)

skylines = reddit.subreddit("skylineporn")
print(skylines.description)

for submission in skylines.hot(limit=None):
    print(submission.title)
    print(submission.url)
    if ".jpg" in submission.url or ".png" in submission.url or ".jpeg" in submission.url:
        response = requests.get(submission.url, stream=True)
        if response.status_code == 200:
            with open(fname, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            break

app('Finder').desktop_picture.set(mactypes.File(fname))


