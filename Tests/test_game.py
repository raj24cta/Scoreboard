import unittest
from football_scoreboard.game import Game


class TestGame(unittest.TestCase):
    def test_game_init(self):
        game = Game("Spain", "Brazil")
        self.assertEqual(game.home_team, "Spain")
        self.assertEqual(game.away_team, "Brazil")
        self.assertEqual(game.home_score, 0)
        self.assertEqual(game.away_score, 0)

    def test_game_update_score(self):
        game = Game("Spain", "Brazil")
        game.update_score(2, 1)
        self.assertEqual(game.home_score, 2)
        self.assertEqual(game.away_score, 1)

    def test_game_get_total_score(self):
        game = Game("Spain", "Brazil")
        game.update_score(2, 1)
        self.assertEqual(game.get_total_score(), 3)

