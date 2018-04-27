import tweepy
import json

class CamTweets:

    _twitter_auth = None
    _tweepy_api = None

    def Authorize(self, auth_path = './auth.json') :
        f = open(auth_path, 'r')
        json_file = f.read()
        config = json.loads(json_file)
        f.close()

        _twitter_auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
        _twitter_auth.set_access_token(config['access_token'], config['token_secret'])
        _tweepy_api = tweepy.API(_twitter_auth)

tweets = CamTweets()
tweets.Authorize()
