#!/usr/bin/env python

"""
swe_twitter.bot
This module handles the business logic of SWE's Twitter bot.
"""

# standard imports
import logging

# global imports
import requests
import twitter

# local imports
from . import settings


class Bot(object):
    def __init__(self):
        self.access_token = settings.ACCESS_TOKEN
        self.access_token_secret = settings.ACCESS_TOKEN_SECRET
        self.consumer_key = settings.CONSUMER_KEY
        self.consumer_key_secret = settings.CONSUMER_SECRET
        # self.log_file = settings.LOG_FILE
        self.url = settings.URL
        self.connection = self.twitter_connection()

    def __repr__(self):
        screen_name = self.connection.VerifyCredentials().screen_name
        text = "{class_name}({screen_name})".format(
            class_name=self.__class__.__name__, screen_name=screen_name)
        return text

    def post_update(self, text):
        """Connect to Twitter and post text."""
        self.connection.PostUpdate(text)

    def swe_request(self):
        """Collect JSON data available at url."""
        logging.info("Connect to SWE API.")
        try:
            data = requests.get(self.url).json()
            return data
        except requests.ConnectionError:
            logging.error("No connection to SWE API possible.")

    def twitter_connection(self):
        """Connect to Twitter API using local settings."""
        logging.info("Connect to Twitter.")
        try:
            connection = twitter.Api(
                consumer_key=self.consumer_key,
                consumer_secret=self.consumer_key_secret,
                access_token_key=self.access_token,
                access_token_secret=self.access_token_secret)
            return connection
        except twitter.TwitterError:
            logging.error("No connection to Twitter profile possible.")
