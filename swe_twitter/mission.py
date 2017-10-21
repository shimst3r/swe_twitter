#!/usr/bin/env python

"""
swe_twitter.mission
This class stores information for each mission used by the bot class.
"""

# standard imports
import datetime
import re

class Mission(object):
    def __init__(self, data):
        self.KO = data["CoName"]
        self.KO_Rang = data["CoRankShort"]
        self.Einheit = data["SquadName"]
        self.TSK = data["SquadType"]
        self.Spielzeit = self.timeTransformer(data["Gametime"])

    def __repr__(self):
        datum = self.Spielzeit.strftime("%d%m%y")
        einheit = self.Einheit
        text = "{class_name}({einheit}, {datum})".format(
            class_name=self.__class__.__name__, einheit=einheit, datum=datum)

        return text

    def __str__(self):
        return {
            "Army": self.armyText(),
            "Navy": self.navyText(),
            "Starfighter Corps": self.sfcText()
        }.get(self.TSK, ValueError)

    def armyText(self):
        text = ("Kämpft als Soldaten des Regiments",
                "{einheit} unter Kommando von".format(einheit=self.Einheit),
                "{rang} {name} zu ZI".format(rang=self.KO_Rang, name=self.KO),
                "{zi} nE um".format(zi=self.Spielzeit.strftime("%d%m%y")),
                "{uhr} SZ für das Imperium!".format(uhr=self.Spielzeit.strftime("%H%M")))

        return " ".join(text)

    def navyText(self):
        text = ("Schließt euch dem Kriegsschiff {einheit}".format(einheit=self.Einheit),
                "unter Kommando von {rang}".format(rang=self.KO_Rang),
                "{name} zu ZI {zi} nE um".format(name=self.KO, zi=self.Spielzeit.strftime("%d%m%y")),
                "{uhr} SZ im Kampf für das Imperium an!".format(uhr=self.Spielzeit.strftime("%H%M")))

        return " ".join(text)

    def sfcText(self):
        text = ("Begleitet die Piloten des Trägers {einheit}".format(einheit=self.Einheit),
                "unter Kommando von {rang}".format(rang=self.KO_Rang),
                "{name} zu ZI {zi} nE um".format(name=self.KO, zi=self.Spielzeit.strftime("%d%m%y")),
                "{uhr} SZ ins Gefecht.".format(uhr=self.Spielzeit.strftime("%H%M")))

        return " ".join(text)

    def timeTransformer(self, time):
        """Converts Gregorian calendar to SWE time format."""
        y, m, d, h, mn, s = [int(_) for _ in re.split(r'[-|T|:]', time)]
        result = datetime.datetime(y + 5, m, d, h, mn, s)
        return result
