#!/usr/bin/env python3

import os
import json
import urllib.request

tweetsdir = "data/js/tweets"
mediadir = "media"

def process_json(js):
    if isinstance(js, list):
        for entry in js:
            process_json(entry) 

    if isinstance(js, dict):
        for key in js:
            if key == "media_url":
                print(js["media_url"])
                filename = download(js["media_url"])
                js["media_url"] = filename

            process_json(js[key])

def file_exists(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        return False

    f.close()
    return True

def filename_from(url):
    keys = ["media/", "tweet_video_thumb/", "/img/"]
    for key in keys:
        if key in url:
            return url.split(key)[1]

    raise Exception("No filename in url" + url)

def download(url): 
    """Download the file from the url and return the filename."""
    filename = filename_from(url)
    filename = os.path.join(mediadir, filename)
    if file_exists(filename):
        print("skipping", filename)
        return filename

    print("loading", url, "->", filename)
    u = urllib.request.urlopen(url)
    bs = u.read()
    with open(filename, "wb") as f:
        f.write(bs)
    return filename    

def main():
    for file in os.listdir(tweetsdir):
        filename = os.path.join(tweetsdir, file)
        print("processing file", filename)
        # read files except first line
        fst, *jsons = open(filename).readlines()
        jsons = "".join(jsons)
        js = json.loads(jsons)
        process_json(js)
        js = json.dumps(js, indent=2)
        js = fst + js
        with open(filename, "w") as f:
            f.write(js)

if __name__ == "__main__":
    main()
