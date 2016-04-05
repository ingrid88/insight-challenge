import json
import pandas as pd
import datetime

def tweet_tag_pairs(date,tag_list):
    combinations = []
    for i in range(len(tag_list)):
        for j in range(i,len(tag_list)):
            tag1 = tag_list[i]
            tag2 = tag_list[j]
            if tag1 != tag2:
                combinations.append((date,tag1,tag2))
    return combinations

def check_duplicates(df):
    t = pd.DataFrame(columns =['f','l','tag1','tag2'])
    t['f'] = df.apply(lambda x: max(x.tag1,x.tag2),axis=1)
    t['l'] = df.apply(lambda x: min(x.tag1,x.tag2),axis=1)
    t['tag1'] = df.tag1
    t['tag2'] = df.tag2
    t['date'] = df.date
    t = t.groupby(by=["f","l"], as_index=False).last()[['date','tag1','tag2']]
    return t
