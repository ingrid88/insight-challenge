import json
import os
import pandas as pd
import datetime
import helper_function as hf
import pickle


def process_tweets(f):

    output = open('./tweet_output/output.txt', 'w')
    max_date = pd.to_datetime(0)
    df_all = pd.DataFrame(columns =["date","tag1","tag2"])
    dataFrameBuilt = False

    for i, line in enumerate(f):
        # load JSON
        d = json.loads(line)
        # retrieve date and hashtag list
        if d.get(u'limit') == None:
            date = pd.to_datetime(d['created_at'])
            max_date = max(date,max_date)
            if len(d['entities']['hashtags']) > 1:
                # retrieve hashtags
                htags = [tag['text'] for tag in d['entities']['hashtags']]

                # build tag pairs from tweet
                pair_list = hf.tweet_tag_pairs(date,htags)

                # dataframe of tweet
                df = pd.DataFrame(pair_list,columns =["date","tag1","tag2"])
                df_all = df_all.append(df)

                # Select all tweets within 60 seconds of max_time
                df_all = df_all[(max_date - df_all.date) < datetime.timedelta(minutes=1)]

                # take into account duplicate pairs at different times
                df_all = df_all.groupby(by=["tag1","tag2"], as_index=False).last()

                # Record these tables and we want to weight the edges ? (aka counting)
                pickle('60_second_interval_'+str(i),df_all)
                # use in a graph of some sort of way in a flask app.

                # Calculate # unique tags
                unique_tags = len(set(list(df_all.tag1)+list(df_all.tag2)))

                # Calculate the connectivity value: (total edges * 2) / (unique tags)
                val = df_all.shape[0]*2 / float(unique_tags)

                # write the value to file
                x = '{0:.2f}'.format(val)
                output.write(x+'\n')
                dataFrameBuilt = True
            else:
                # even if there is zero or no hashtag in this tweet,
                # we still want to record the running total,
                # which is just the same as the previous one

                if dataFrameBuilt == False:
                    val = 0
                else:
                    val = df_all.shape[0]*2 / float(unique_tags)
                x = '{0:.2f}'.format(val)
                output.write(x+'\n')

if __name__ == '__main__':

    tweets_file = './tweet_input/tweets.txt'
    f = open(tweets_file, 'r')
    process_tweets(f)
    f.close()
