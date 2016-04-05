Insight Data Engineering - Coding Challenge
===========================================================

## requirements for average_degree.py
import json
import pandas as pd
import datetime
import helper_function as hf

## Implementation / design
We create an adjacency list to store the edges built by each tweet - hashtag graph
1. open tweets and read each json element at a time
- if the json element is not a tweet, we skip it
- if the json element has more than 1 tweet we call a helper method tweet tag pairs which generates all edges
3. we store edges and their corresponding date in a pandas data frame
4. we select only the most recent 60 seconds of tweets and then calculate the rolling average degree
- because our graph is an adjacency list we can calculate this from 2 x the number of edges divided by the number of unique nodes (hashtags) in the dataframe of the last 60 second hashtag edges.
5. we take care of a few edge cases
- edge created at two distinct times (take only most recent one within 60 second interval)

## Unit Tests
1. is the code being run in under a minute per minute of sequence?
2. write out an error log?  (try except)

#### there is a separate readme for the get-tweets.py
