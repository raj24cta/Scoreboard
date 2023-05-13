import unittest
from football_scoreboard.game import Game
from football_scoreboard.scoreboard import Scoreboard


class TestScoreboard(unittest.TestCase):
    def setUp(self):
        self.scoreboard = Scoreboard()

    def test_scoreboard_start_game(self):
        self.scoreboard.start_game("Spain", "Brazil")
        self.assertEqual(len(self.scoreboard.games), 1)
        game = self.scoreboard.games[0]
        self.assertEqual(game.home_team, "Spain")
        self.assertEqual(game.away_team, "Brazil")
        self.assertEqual(game.home_score, 0)
        self.assertEqual(game.away_score, 0)

    def test_scoreboard_update_score(self):
        self.scoreboard.start_game("Spain", "Brazil")
        self.scoreboard.update_score(0, 2, 1)
        game = self
