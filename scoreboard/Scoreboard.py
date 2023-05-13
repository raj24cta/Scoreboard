from collections import defaultdict


class Scoreboard:
    def __init__(self):
        self.matches = []

    def start_game(self, home_team, away_team):
        game = Game(home_team, away_team)
        self.matches.append(game)

    def update_score(self, home_score, away_score):
        if len(self.matches) == 0:
            raise ValueError("No matches in progress")

        current_game = self.matches[-1]
        current_game.update_score(home_score, away_score)

    def finish_game(self):
        if len(self.matches) == 0:
            raise ValueError("No matches in progress")

        self.matches.pop()

    def get_summary(self):
        summary = sorted(self.matches, key=lambda x: x.total_score(), reverse=True)
        return summary


class Game:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0

    def update_score(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score

    def total_score(self):
        return self.home_score + self.away_score

