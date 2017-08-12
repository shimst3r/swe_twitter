# imports from standard libraries
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
        fields = {"CoName", "CoRankShort", "Gametime","SquadName", "SquadType"}
        for entry in self.data:
            for field in fields:
                self.assertIn(field, entry.keys())

    # TODO: Test cases for mission class

if __name__ == "__main__":
    unittest.main()
