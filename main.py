import click
from scoreboard.scoreboard import Scoreboard


@click.group()
def cli():
    pass


@cli.command()
@click.option("--home", prompt="Home Team", help="Name of the home team")
@click.option("--away", prompt="Away Team", help="Name of the away team")
def start(home, away):
    scoreboard.start_match(home, away)
    click.echo("Match started successfully!")


@cli.command()
@click.option("--home", prompt="Home Team", help="Name of the home team")
@click.option("--away", prompt="Away Team", help="Name of the away team")
@click.option("--home-score", prompt="Home Team Score", type=int, help="Home team score")
@click.option("--away-score", prompt="Away Team Score", type=int, help="Away team score")
def update(home, away, home_score, away_score):
    scoreboard.update_score(home, away, home_score, away_score)
    click.echo("Score updated successfully!")


@cli.command()
@click.option("--home", prompt="Home Team", help="Name of the home team")
@click.option("--away", prompt="Away Team", help="Name of the away team")
def finish(home, away):
    scoreboard.finish_match(home, away)
    click.echo("Match finished successfully!")


@cli.command()
def summary():
    summary = scoreboard.get_summary()
    click.echo("Summary of ongoing matches:")
    for i, match in enumerate(summary, start=1):
        click.echo(f"{i}. {match.home_team} {match.home_score} - {match.away_team} {match.away_score}")


if __name__ == "__main__":
    scoreboard = Scoreboard()
    cli()

