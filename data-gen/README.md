# Data Generator with Real Twitter Data

## requirements for get-tweets.py
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json
import os
import tweepy
from requests_oauthlib import OAuth1
import cnfg
