import unittest
from scoreboard.scoreboard import Scoreboard


class ScoreboardTestCase(unittest.TestCase):
    def setUp(self):
        self.scoreboard = Scoreboard()

    def test_start_game(self):
        self.scoreboard.start_game("Mexico", "Canada")
        self.assertEqual(len(self.scoreboard.matches), 1)

    def test_update_score(self):
        self.scoreboard.start_game("Mexico", "Canada")
        self.scoreboard.update_score(0, 5)
        current_game = self.scoreboard.matches[-1]
        self.assertEqual(current_game.home_score, 0)
        self.assertEqual(current_game.away_score, 5)

    def test_finish_game(self):
        self.scoreboard.start_game("Mexico", "Canada")
        self.scoreboard.finish_game()
        self.assertEqual(len(self.scoreboard.matches), 0)

    def test_get_summary(self):
        self.scoreboard.start_game("Mexico", "Canada")
        self.scoreboard.update_score(0, 5)
        self.scoreboard.start_game("Spain", "Brazil")
        self.scoreboard.update_score(10, 2)
        self.scoreboard.start_game("Germany", "France")
        self.scoreboard.update_score(2, 2)
        self.scoreboard.start_game("Uruguay", "Italy")
        self.scoreboard.update_score(6, 6)
        self.scoreboard.start_game("Argentina", "Australia")
        self.scoreboard.update_score(3, 1)
        summary = self.scoreboard.get_summary()
        self.assertEqual(summary[0].

