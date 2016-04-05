import json
import pandas as pd
import datetime

def tweet_tag_pairs(date,tag_list):
    combinations = []
    tag_list = sorted(tag_list)
    for i in range(len(tag_list)):
        for j in range(i,len(tag_list)):
            tag1 = tag_list[i]
            tag2 = tag_list[j]
            if tag1 != tag2:
                combinations.append((date,tag1,tag2))
    return combinations
