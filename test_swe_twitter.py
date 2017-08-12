# imports from standard libraries
import unittest

# imports from global libraries


# imports from local libraries
import swe_twitter.run_bot
import swe_twitter.settings


class TestConnectionMethods(unittest.TestCase):
    """This class is responsible for testing database and Twitter connections.
    """
    def test_swe_request(self):
        """Test if SWE request returns any data."""
        data = swe_twitter.run_bot.swe_request(swe_twitter.settings.URL)
        self.assertIsNotNone(data)


if __name__ == "__main__":
    unittest.main()
