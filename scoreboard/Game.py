class Game:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0

    def update_score(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score

    def get_total_score(self):
        return self.home_score + self.away_score

    def __str__(self):
        return f"{self.home_team} {self.home_score} - {self.away_team} {self.away_score}"

