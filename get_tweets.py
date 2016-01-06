## Daan Disselhorst
## s1683764
## Information Retrieval 
## Usage: python3 get_tweets.py

import tweepy
import json

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # vul alle benodigde twitter dev account informatie in
  cfg = {
    "consumer_key"        : "blabla",
    "consumer_secret"     : "blabla",
    "access_token"        : "blabla",
    "access_token_secret" : "blabla"
    }

  twitApi = get_api(cfg)

  maxTweets = 2000
  zoekTerm = 'Star Wars'
  gevondenTweets = [status._json for status in tweepy.Cursor(twitApi.search,  q=zoekTerm).items(maxTweets)]

  with open('big_tweet_file/starwar.txt', 'w') as outBestand:
    json.dump(gevondenTweets, outBestand)

if __name__ == "__main__":
  main()

