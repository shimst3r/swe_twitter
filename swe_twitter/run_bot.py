#!/usr/bin/env python

"""
swe_twitter.run_bot
This module is a wrapper for running the Twitter bot.
"""

# standard imports
import datetime
import logging

# global imports
import schedule

# local imports
from . import bot, mission, settings

# Format string for datetime.datetime.strptime
strptime_fmt = "%Y-%m-%dT%H:%M:%S"

def bot_job(my_bot):
    """Job executed by scheduler."""
    data = my_bot.swe_request()
    logging.info("Connect to SWE API.")
    todays_missions = [entry for entry in filter_data(data,datetime.datetime.now().date())]

def filter_data(data, date):
    """Go through data and yield entries corresponding to date."""
    for entry in data:
        entry_date = datetime.datetime.strptime(entry["Gametime"], strptime_fmt).date()
        if entry_date + datetime.timedelta(days=1) == date:
            yield entry

def run_bot():
    """Initialize bot and start loop."""
    logging.basicConfig(filename=settings.LOGGER,
                    format="%(asctime)s :: %(levelname)s -> %(message)s",
                    level=logging.INFO)
    my_bot = bot.Bot()
    logging.info("Created {bot}".format(bot=my_bot))

    while 1:
        schedule.every().day.at("23:59").do(bot_job(my_bot))

if __name__ == "__main__":
    run_bot()
