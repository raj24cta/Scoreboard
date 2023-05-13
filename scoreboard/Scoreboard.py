class Scoreboard:
    def __init__(self):
        self.games = []

    def start_game(self, home_team, away_team):
        game = Game(home_team, away_team)
        self.games.append(game)

    def update_score(self, game_index, home_score, away_score):
        game = self.games[game_index]
        game.update_score(home_score, away_score)

    def finish_game(self, game_index):
        self.games.pop(game_index)

    def get_summary(self):
        sorted_games = sorted(self.games, key=lambda g: (-g.get_total_score(), -self.games.index(g)))
        return "\n".join([f"{i+1}. {game}" for i, game in enumerate(sorted_games)])
