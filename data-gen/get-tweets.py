#!/usr/bin/env python

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json
import os
import tweepy
from requests_oauthlib import OAuth1
import cnfg

# loads Twitter credentials from .twitter file that is in the same directory as this script
file_dir = os.path.dirname(os.path.realpath(__file__))
config = cnfg.load(file_dir + '/.twitter')

# authentication from the credentials file above
oauth = OAuth1(config["consumer_key"],
               config["consumer_secret"],
               config["access_token"],
               config["access_token_secret"])


class StdOutListener(StreamListener):
    """ A listener handles tweets that are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, filename):
        self.filename = filename

    # this is the event handler for new data
    def on_data(self, data):
        if not os.path.isfile(self.filename):    # check if file doesn't exist
            f = file(self.filename, 'w')
            f.close()
        with open(self.filename, 'ab') as f:
            f.write(data)
        f.closed

    # this is the event handler for errors
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener(file_dir + "/tweets.txt")

    auth = tweepy.OAuthHandler(config["consumer_key"],
                               config["consumer_secret"])
    auth.set_access_token(config["access_token"],
                          config["access_token_secret"])

    print "Use CTRL + C to exit at any time.\n"
    stream = Stream(auth, listener)
    stream.filter(locations=[-180,-90,180,90]) # this is the entire world, any tweet with geo-location enabled
