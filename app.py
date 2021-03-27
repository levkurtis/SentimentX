# API Key - xBiIbQYUBVf7AiObJ5EKm4NOK
# API secret key - iwKf6r4Oq1NsZ1OKSPy2awYUXxrZ6hRvV6tFm0244Ytc7yZDHE
# Bearer token - AAAAAAAAAAAAAAAAAAAAAMvPMAEAAAAAChRaocQymcY2VGpsXBvX4UZeHnM%3DPJ725Hx6HuMTTdcnbcXMoRFx8OBDZTor3bNj7UJwmpzEmwDcwI
# Access token - 1251111873967259648-FgJDabTBEn6pjxYLkdkmgePNn14nlx
# Access token secret - 5dUk278eRLMGJrfye8rsYRrqlwZtMB2GdA1cJSaU9PdUk

# keys and tokens from the Twitter Dev Console
import twitter

twitter_consumer_key = 'xBiIbQYUBVf7AiObJ5EKm4NOK'
twitter_consumer_secret = 'iwKf6r4Oq1NsZ1OKSPy2awYUXxrZ6hRvV6tFm0244Ytc7yZDHE'
twitter_access_token = '1251111873967259648-FgJDabTBEn6pjxYLkdkmgePNn14nlx'
twitter_access_secret = '5dUk278eRLMGJrfye8rsYRrqlwZtMB2GdA1cJSaU9PdUk'
twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
# handle meaning username
handle = 'cnnbrk'
statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
print(statuses)

hashtags_to_track = 'climate change'
stream = twitter_api.GetStreamFilter (track = hashtags_to_track)
for line in stream:
    if 'in_reply_to_status_id' in line:
        tweet = twitter.Status.NewFromJsonDict(line)
        user = tweet.user.screen_name
        tweet_text = tweet.text
        print('User: ' + user[0] + '\t Tweet: ' + tweet_text + '\n')