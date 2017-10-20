# imports from standard libraries
import collections
import unittest

# imports from global libraries


# imports from local libraries
import swe_twitter.bot
import swe_twitter.mission


class TestBot(unittest.TestCase):
    """Basic test bot template."""
    def setUp(self):
        """Setup everything (unittest method)."""
        self.bot = swe_twitter.bot.Bot()
        self.connection = self.bot.twitter_connection()
        self.data = self.bot.swe_request()

    def tearDown(self):
        """Destroy everything (unittest method)."""
        pass


class TestConnectionMethods(TestBot):
    """This class is responsible for testing database and Twitter connections.
    """
    def test_swe_request_returns_data(self):
        self.assertIsNotNone(self.data)

    def test_twitter_connection_positive(self):
        self.assertIsNotNone(self.connection)

    def test_twitter_screen_name_correct(self):
        self.assertEqual("SWE_3PO",
                         self.connection.VerifyCredentials().screen_name)

    def test_swe_data_contains_relevant_data(self):
        fields = {"CoName", "CoRankShort", "Gametime",
                  "SquadName", "SquadType"}
        for entry in self.data:
            for field in fields:
                self.assertIn(field, entry.keys())

    def test_mission_has_all_attributes(self):
        test_mission = swe_twitter.mission.Mission(self.data[0])
        KO = test_mission.KO
        KO_Rang = test_mission.KO_Rang
        Einheit = test_mission.Einheit
        TSK = test_mission.TSK
        Spielzeit = test_mission.Spielzeit
        pass

    def test_army_mission_displayed_correctly(self):
        mission_data = {"Gametime":"2017-10-22T20:00:00","Story":"...",
                        "Title":"","SquadName":"Stormangels","SquadType":"Army",
                        "CoName":"Valera-Kelley","CoFirstName":"Nyah",
                        "CoRank":"Major General","CoRankShort":"MajGen"}
        mission_instance = swe_twitter.mission.Mission(mission_data)
        mission_str = ""
        self.assertEquals(str(mission_instance), mission_str)

    def test_navy_mission_displayed_correctly(self):
        mission_data = {"Gametime":"2017-10-20T21:00:00",
                        "Story":"Regulärer Spieltermin","Title":"",
                        "SquadName":"TSD Darkness","SquadType":"Navy",
                        "CoName":"Marae","CoFirstName":"Darth",
                        "CoRank":"Sith Lord","CoRankShort":"SL"}
        mission_instance = swe_twitter.mission.Mission(mission_data)
        mission_str = ""
        self.assertEquals(str(mission_instance), mission_str)

    def test_sfc_mission_displayed_correctly(self):
        mission_data = {"Gametime":"2017-11-07T20:00:00","Story":"-","Title":"",
                        "SquadName":"Jackhammer II",
                        "SquadType":"Starfighter Corps","CoName":"Dalyas",
                        "CoFirstName":"Kren","CoRank":"Sentinel",
                        "CoRankShort":"Se"}
        mission_instance = swe_twitter.mission.Mission(mission_data)
        mission_str = ""
        self.assertEquals(str(mission_instance), mission_str)

    def test_bot_can_post_to_twitter_wall(self):
        test_status = "Test"
        self.bot.post_update(test_status)
        latest_tweet = next(tweet
                            for tweet in self.connection.GetHomeTimeline()
                            if tweet.user.screen_name == "SWE_3PO")
        self.assertEqual(test_status, latest_tweet.text)
        self.connection.DestroyStatus(latest_tweet.id)

if __name__ == "__main__":
    unittest.main()
