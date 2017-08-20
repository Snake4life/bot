"""
the twit package is a bear python-twitter adapter
"""
import json
import twitter
from config import twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_secret
import db


api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token,
                  access_token_secret=twitter_access_secret)


# get_recent_tweets_with_search_term returns 100 search results per term
def search(term):
    return api.GetSearch(term=term, count=100, result_type="recent")


# gets a twitter user, aka tweep.
def get_tweep(tweep):
    return api.GetUser(tweep)


# gets top trending hash tags of the moment
def get_trends_for_woeid(place):
    return api.GetTrendsWoeid(place)


# get_avg_api_res returns the logged average api response time for twitter
def get_avg_api_res():
    moon_call_ops = db.get(path="operations", file_name="moon_call")

    durations = 0
    for operation in moon_call_ops:
        start = int(operation["twitter_search_start"])
        end = int(operation["twitter_search_end"])

        durations += abs(start - end)

    avg_res = durations / len(moon_call_ops)

    if avg_res is None:
        print "[WARN] missing average response time from twitter, setting to 30 minutes."
        avg_res = 1800
    else:
        print "[INFO] average twitter response time at " + str(avg_res) + " seconds."

    return avg_res
