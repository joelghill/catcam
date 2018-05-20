from tweet_composer import TweetComposer

predictions = {}
predictions["object 1"] = 0
predictions["object 3"] = 0
predictions["object 4"] = 0
predictions["object 5"] = 0
predictions["object 6"] = 0
predictions["object 2"] = 0

composer = TweetComposer('./tweets.json')
print(composer.get_flavor_text_tweet(predictions))
