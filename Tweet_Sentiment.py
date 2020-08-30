# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 02:58:03 2020

@author: Eduardo Adachi
"""

import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List


consumer_key = "VeTCRY2L0tSIB21emOFcDl6e2"
consumer_secret = "zuckpBfh19hhn2TPwBbYcysnkI0SIeDZ9lk3rANDZAEe4UNspu"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)



def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(10):
        all_tweets.append(tweet.full_text)
        
    return all_tweets

def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))

    return tweets_clean

def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
        
    return sentiment_scores

def generate_avarege_sentiment_score(keyword: str) -> int:
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    sentiment_scores = get_sentiment(tweets_clean)
    
    avarege_score = statistics.mean(sentiment_scores)
    
    return avarege_score


if __name__ == "__main__":
    
    print("What does the word prefer?")
    first_thing = input()
    print("...or...")
    second_thing = input()
    print("\n")
    
    first_score = generate_avarege_sentiment_score(first_thing)
    second_score = generate_avarege_sentiment_score(second_thing)
    
    if(first_score > second_score):
        print(f"The humanity prefers {first_thing} ({first_score}) over {second_thing} ({second_score})!")
    else:
        print(f"The humanity prefers {second_thing} ({second_score}) over {first_thing} ({first_score})!")
