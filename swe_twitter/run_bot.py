#!/usr/bin/env python

"""
swe_twitter.run_bot
This module handles the business logic of SWE's twitter bot.
"""

# global imports
import requests

# local imports


def swe_request(url):
    """Collect JSON data available at url."""
    data = requests.get(url).json()
    return data
