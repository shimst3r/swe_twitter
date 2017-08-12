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

    def tearDown(self):
        """Destroy everything (unittest method)."""
        pass


class TestConnectionMethods(TestBot):
    """This class is responsible for testing database and Twitter connections.
    """
    def test_swe_request(self):
        """Test if SWE request returns any data."""
        data = self.bot.swe_request()
        self.assertIsNotNone(data)

    def test_twitter_connection(self):
        """Test if bot is able to connect to Twitter API."""
        self.assertIsNotNone(self.connection)

    def test_twitter_screen_name(self):
        """Test if bot is connected with correct credentials."""
        self.assertEquals("SWE_3PO",
                          self.connection.VerifyCredentials().screen_name)

    def test_mission_object_has_correct_structure(self):
        """Test if mission is of the correct type."""
        mission = None
        self.assertIsInstance(mission, swe_twitter.mission.Mission)

if __name__ == "__main__":
    unittest.main()
