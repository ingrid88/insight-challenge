## open tweets.txt
import json
import os
import pprint
tweets_file = './tweet_input/tweets.txt'

f = open(tweets_file, 'r')
dates =[]
htag_lists=[]
for line in f:
    d = json.loads(line)
    date = d['created_at']
    dates.append(date)
    htags = [tag['text'] for tag in d['entities']['hashtags']]
    htags.append(date)

## build graph or add to graph

## RULES ##
## 1. remove all edges created at time less than max - 60
## 2. update time stamp of all edges if they are made later on
## 3. When we add / remove edges we dont necessarily need to recommpute the average
## 4.
## compute graph
### res

if __name__ == '__main__':

## write output.txt
    f = open('./tweet_output/output.txt', 'w')
    print f
    res = [1.00,2.33]
    for val in res:
        x = '{0:.2f}'.format(val)
        f.write(x+'\n')

    f.close()
