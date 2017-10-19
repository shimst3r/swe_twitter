#!/usr/bin/env python

"""
swe_twitter.run_bot
This module handles the business logic of SWE's twitter bot.
"""

# global imports
import requests
import twitter

# local imports
from . import settings


class Bot(object):
    def __init__(self):
        self.access_token = settings.ACCESS_TOKEN
        self.access_token_secret = settings.ACCESS_SECRET_TOKEN
        self.consumer_key = settings.CONSUMER_KEY
        self.consumer_key_secret = settings.CONSUMER_SECRET
        # self.log_file = settings.LOG_FILE
        self.url = settings.URL

    def post_update(self, text):
        connection = self.twitter_connection()
        connection.PostUpdate(text)

    def swe_request(self):
        """Collect JSON data available at url."""
        data = requests.get(self.url).json()
        return data

    def twitter_connection(self):
        """Connect to Twitter API using local settings."""
        connection = twitter.Api(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_key_secret,
            access_token_key=self.access_token,
            access_token_secret=self.access_token_secret)
        return connection
