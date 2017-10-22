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

def bot_job(my_bot):
    """Job executed by scheduler."""
    data = my_bot.swe_request()
    todays_missions = {mission.Mission(entry) for entry
                       in bot.filter_data(data,datetime.datetime.now().date())}
    logging.info("Found {amount} entries.".format(amout=len(todays_missions)))

    for mission in todays_missions:
        my_bot.post_update(str(mission))
        logging.info("Sent tweet {mission}".format(mission=repr(mission)))


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
