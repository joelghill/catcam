import tweepy
import json

class CamTweets:

    _twitter_auth = None
    _tweepy_api = None

    def authorize(self, auth_path = './auth.json') :
        try:
            f = open(auth_path, 'r')
            json_file = f.read()
            config = json.loads(json_file)
            f.close()

            self._twitter_auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
            self._twitter_auth.set_access_token(config['access_token'], config['token_secret'])
            self._tweepy_api = tweepy.API(self._twitter_auth)
        except Exception as e:
            print("Failed to authorize twitter account: " + str(e))

    def update_timeline(self, text, image_path) :
        try:
            self._tweepy_api.update_with_media(image_path, text)
        except Exception as e:
            print('Failed to update timeline: ' + str(e))

#tweets = CamTweets()
#tweets.authorize()
#tweets.update_timeline("TEST POST FROM RASPBERRY PI. PLEASE IGNORE.", "./test.jpg")
