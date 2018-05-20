import json
import random


class TweetComposer:
    """
    Composes tweets
    """
    _tweets_path = ""
    _flavor_text_odds = 0
    _tweets = None

    def __init__(self, tweets_path='./tweets.json', flavour_text_odds=50):
        """
        Constructs a new instance of the TweetComposer class
        :type flavour_text_odds: object
        :type tweets_path: basestring
        """
        self._tweets_path = tweets_path
        self._flavor_text_odds = flavour_text_odds
        self._load_tweets()

    def compose_tweet(self, predictions):
        """
        Composes a tweet based on the predicted content of an image
        :param predictions: The predicted content of an image
        :return: A tweet ready to send out into the world
        """
        random_value = random.randint(0, 100)
        if random_value >= self._flavor_text_odds:
            return self.get_flavor_text_tweet(predictions)
        else:
            return TweetComposer.get_default_tweet(predictions)

    def get_flavor_text_tweet(self, predictions):
        """
        Gets a tweet containing flavored text
        :type predictions: object
        """
        tweet_object = random.choice(self._tweets)
        keys = predictions.keys()
        text = tweet_object["message"].format(keys[0], keys[1], keys[2])
        return text

    @staticmethod
    def get_default_tweet(predictions):
        """
        Gets the default tweet text
        :type predictions: object
        """
        first_guess_name = predictions.keys()[0]
        first_guess_value = predictions.values()[0]
        second_guess = predictions.keys()[1]

        text = "I'm {0:.2%} confident this is a {1}. Might be a {2}"\
            .format(first_guess_value, first_guess_name, second_guess)

        return text

    def _load_tweets(self):
        """
        Loads the list of tweet objects from disk
        """
        with open(self._tweets_path) as f:
            self._tweets = json.load(f)
