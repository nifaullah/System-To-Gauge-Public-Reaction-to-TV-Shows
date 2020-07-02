# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:22:53 2020

@author: nifaullah
"""


import pandas as pd
import GetOldTweets3 as got # ! pip install GetOldTweets3
from datetime import datetime, timedelta
from tqdm import tqdm # ! pip install tqdm

# series - name of the tv series
# season - current season
# past_days - how many days of the data do you want
# max_tweets_per_call - Number of tweets for each day
def GetTweets(series, season, past_days, max_tweets_per_call = 1000):
    start_date = datetime.today().date()
    end_date = datetime.today().date() +  timedelta(days = 1)
    tweets_lst = []
    for i in tqdm(range(0,past_days)):
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(series)\
                                               .setSince(start_date.strftime("%Y-%m-%d"))\
                                               .setUntil(end_date.strftime("%Y-%m-%d"))\
                                               .setWithin("1000")\
                                               .setMaxTweets(max_tweets_per_call)
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        tweets_lst.extend(tweets)
        start_date = start_date -  timedelta(days = 1)
        end_date = end_date -  timedelta(days = 1)
    variables = ["id", "permalink", "username", "text", "date", "retweets", "favorites"]
    df = pd.DataFrame([[getattr(i,j) for j in variables] for i in tweets_lst], columns = variables)
    df["series"] = series
    df["sentiment"] = 1
    df["season"] = 4
    df.to_csv(f"{series}_{len(df)}_tweets.csv", index = False)
    return df