import unittest
from scoreboard.scoreboard import Scoreboard


class TestScoreboard(unittest.TestCase):
    def setUp(self):
        self.scoreboard = Scoreboard()

    def test_start_match(self):
        self.scoreboard.start_match("Mexico", "Canada")
        matches = self.scoreboard.get_summary()
        self.assertEqual(len(matches), 1)
        match = matches[0]
        self.assertEqual(match.home_team, "Mexico")
        self.assertEqual(match.away_team, "Canada")
        self.assertEqual(match.home_score, 0)
        self.assertEqual(match.away_score, 0)

    def test_update_score(self):
        self.scoreboard.start_match("Mexico", "Canada")
        self.scoreboard.update_score("Mexico", "Canada", 2, 1)
        matches = self.scoreboard.get_summary()
        self.assertEqual(len(matches), 1)
        match = matches[0]
        self.assertEqual(match.home_score, 2)
        self.assertEqual(match.away_score, 1)

    def test_finish_match(self):
        self.scoreboard.start_match("Mexico", "Canada")
        self.scoreboard.finish_match("Mexico", "Canada")
        matches = self.scoreboard.get_summary()
        self.assertEqual(len(matches), 0)

    def test_get_summary(self):
        self.scoreboard.start_match("Mexico", "Canada")
        self.scoreboard.start_match("Spain", "Brazil")
        self.scoreboard.update_score("Mexico", "Canada", 3, 1)
        self.scoreboard.update_score("Spain", "Brazil", 2, 2)
        matches = self.scoreboard.get_summary()
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0].home_team, "Mexico")
        self.assertEqual(matches[0].away_team, "Canada")
        self.assertEqual(matches[1].home_team, "Spain")
        self.assertEqual(matches[1].away_team, "Brazil")
        self.assertGreater(matches[0].home_score, matches[1].home_score)


if __name__ == '__main__':
    unittest.main()
