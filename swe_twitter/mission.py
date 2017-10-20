import datetime
import re

class Mission(object):
    def __init__(self, data):
        self.KO = data["CoName"]
        self.KO_Rang = data["CoRank"]
        self.Einheit = data["SquadName"]
        self.TSK = data["SquadType"]
        time = re.split(r'[-|T|:]', data["Gametime"])
        y, m, d, h, mn, s = [int(_) for _ in time]
        self.Spielzeit = datetime.datetime(y, m, d, h, mn, s)

    def __str__(self):
        return {
            "Army": ArmyText(self),
            "Navy": NavyText(self),
            "Starfighter Corps": SFCText(self)
        }.get(self.TSK, ValueError)
