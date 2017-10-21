# imports from standard libraries
import datetime
import re
import unittest

# imports from global libraries


# imports from local libraries
import swe_twitter.bot
import swe_twitter.mission


class TestBot(unittest.TestCase):
    """Basic test bot template."""
    def setUp(self):
        self.bot = swe_twitter.bot.Bot()
        self.connection = self.bot.twitter_connection()
        self.data = self.bot.swe_request()

    def tearDown(self):
        pass


class TestConnection(TestBot):
    """This class is responsible for testing database and Twitter connections.
    """
    def test_swe_request_returns_data(self):
        self.assertIsNotNone(self.data)

    def test_swe_data_contains_relevant_data(self):
        fields = {"CoName", "CoRankShort", "Gametime",
                  "SquadName", "SquadType"}
        for entry in self.data:
            for field in fields:
                self.assertIn(field, entry.keys())

    def test_twitter_connection_positive(self):
        self.assertIsNotNone(self.connection)

    def test_twitter_screen_name_correct(self):
        self.assertEqual("SWE_3PO",
                         self.connection.VerifyCredentials().screen_name)


class TestMissionClass(TestBot):
    """This class is responsible for testing all methods of Mission."""
    def test_mission_has_all_attributes(self):
        mission_data = {"Gametime":"2017-01-01T20:00:00","Story":"...",
                        "Title":"","SquadName":"ArmySquad","SquadType":"Army",
                        "CoName":"Test", "CoFirstName":"Test",
                        "CoRank":"General","CoRankShort":"Gen"}
        test_mission = swe_twitter.mission.Mission(mission_data)
        time = re.split(r'[-|T|:]', mission_data["Gametime"])
        y, m, d, h, mn, s = [int(_) for _ in time]
        date = datetime.datetime(y + 5, m, d, h, mn, s)
        self.assertEqual(mission_data["CoName"], test_mission.KO)
        self.assertEqual(mission_data["CoRankShort"], test_mission.KO_Rang)
        self.assertEqual(mission_data["SquadName"], test_mission.Einheit)
        self.assertEqual(mission_data["SquadType"], test_mission.TSK)
        self.assertEqual(date, test_mission.Spielzeit)

    def test_mission_internal_representation(self):
        mission_data = {"Gametime":"2017-01-01T20:00:00","Story":"...",
                        "Title":"","SquadName":"ArmySquad","SquadType":"Army",
                        "CoName":"Test", "CoFirstName":"Test",
                        "CoRank":"General","CoRankShort":"Gen"}
        mission_instance = swe_twitter.mission.Mission(mission_data)
        mission_repr = "Mission(ArmySquad, 010122)"
        self.assertEqual(repr(mission_instance), mission_repr)

    def test_army_mission_displayed_correctly(self):
        mission_data = {"Gametime":"2017-01-01T20:00:00","Story":"...",
                        "Title":"","SquadName":"ArmySquad","SquadType":"Army",
                        "CoName":"Test", "CoFirstName":"Test",
                        "CoRank":"General","CoRankShort":"Gen"}
        mission_instance = swe_twitter.mission.Mission(mission_data)
        mission_str = ("Kämpft als Soldaten des Regiments ArmySquad "
                       "unter Kommando von Gen Test zu ZI 010122 nE um "
                       "2000 SZ für das Imperium!")
        self.assertEqual(str(mission_instance), mission_str)

    def test_navy_mission_displayed_correctly(self):
        mission_data = {"Gametime":"2017-01-01T20:00:00","Story":"...",
                        "Title":"","SquadName":"NavySquad","SquadType":"Navy",
                        "CoName":"Test", "CoFirstName":"Test",
                        "CoRank":"Admiral","CoRankShort":"Adm"}
        mission_instance = swe_twitter.mission.Mission(mission_data)
        mission_str = ("Schließt euch dem Kriegsschiff NavySquad unter "
                       "Kommando von Adm Test zu ZI 010122 nE um "
                       "2000 SZ im Kampf für das Imperium an!")
        self.assertEqual(str(mission_instance), mission_str)

    def test_sfc_mission_displayed_correctly(self):
        mission_data = {"Gametime":"2017-01-01T20:00:00","Story":"...",
                        "Title":"","SquadName":"SFCSquad",
                        "SquadType":"Starfighter Corps",
                        "CoName":"Test", "CoFirstName":"Test",
                        "CoRank":"Marshal","CoRankShort":"Ma"}
        mission_instance = swe_twitter.mission.Mission(mission_data)
        mission_str = ("Begleitet die Piloten des Trägers SFCSquad "
                       "unter Kommando von Ma Test zu ZI 010122 "
                       "nE um 2000 SZ ins Gefecht.")
        self.assertEqual(str(mission_instance), mission_str)

    def test_mission_text_shorter_than_140_characters(self):
        for entry in self.data:
            test_mission = swe_twitter.mission.Mission(entry)
            self.assertLessEqual(len(str(test_mission)), 140)

class TestBotClass(TestBot):
    """This class is responsible for testing all methods of class Bot."""
    def test_bot_internal_representation(self):
        bot_repr = "Bot(SWE_3PO)"
        self.assertEqual(bot_repr, repr(self.bot))

    def test_bot_can_post_to_twitter_wall(self):
        test_status = "Test"
        self.bot.post_update(test_status)
        latest_tweet = next(tweet
                            for tweet in self.connection.GetHomeTimeline()
                            if tweet.user.screen_name == "SWE_3PO")
        self.assertEqual(test_status, latest_tweet.text)
        self.connection.DestroyStatus(latest_tweet.id)

class TestRunBot(TestBot):
    """This class is responsible for testing the run_bot script."""
    def test_filter_data_filters_correctly(self):
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
