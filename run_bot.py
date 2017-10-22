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
from swe_twitter import bot, mission, settings

# Format string for datetime.datetime.strptime
strptime_fmt = "%Y-%m-%dT%H:%M:%S"

def bot_job():
    """Job executed by scheduler."""
    my_bot = bot.Bot()
    logging.info("Created {bot}".format(bot=my_bot))
    data = my_bot.swe_request()
    todays_missions = {mission.Mission(entry) for entry
                       in filter_data(data,datetime.datetime.now().date())}
    logging.info("Found {amount} entries.".format(amount=len(todays_missions)))

    for entry in todays_missions:
        my_bot.post_update(str(entry))
        logging.info("Sent tweet {mission}".format(mission=repr(entry)))

def filter_data(data, date):
        """Go through data and yield entries corresponding to date."""
        for entry in data:
            entry_date = datetime.datetime.strptime(entry["Gametime"], strptime_fmt).date()
            if date + datetime.timedelta(days=1) == entry_date:
                yield entry

def run_bot():
    """Initialize bot and start loop."""
    logging.basicConfig(filename=settings.LOGGER,
                    format="%(asctime)s :: %(levelname)s -> %(message)s",
                    level=logging.INFO)

    bot_job()

    # while 1:
    #     schedule.every().day.at("23:59").do(bot_job)

if __name__ == "__main__":
    run_bot()
