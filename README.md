Live Football World Cup Scoreboard
This is a Python library for managing and displaying live scores of ongoing matches in a Football World Cup. The library provides functionalities to start a new game, update scores, finish a game, and get a summary of ongoing matches.

Installation
To use this library, you can simply clone the repository or download the source code files to your local machine.

Dependencies
This library has the following dependencies:

Python 3.x
click (for the command-line interface)
You can install the dependencies by running the following command:

bash
Copy code
pip install -r requirements.txt
Usage
To use the library, you can import the Scoreboard class from the scoreboard.scoreboard module. Here's an example:

python
Copy code
from scoreboard.scoreboard import Scoreboard

# Create a new instance of the Scoreboard class
scoreboard = Scoreboard()

# Start a new match
scoreboard.start_match("Mexico", "Canada")

# Update scores
scoreboard.update_score("Mexico", "Canada", 0, 5)

# Finish a match
scoreboard.finish_match("Mexico", "Canada")

# Get a summary of ongoing matches
summary = scoreboard.get_summary()
for match in summary:
    print(f"{match.home_team} {match.home_score} - {match.away_team} {match.away_score}")
Command-Line Interface
The library also provides a command-line interface for easy interaction. You can run the main.py script to access the command-line interface. Here are the available commands:

start: Start a new match.
update: Update scores of a match.
finish: Finish a match.
summary: Get a summary of ongoing matches.
Example usage:

bash
Copy code
python main.py start --home "Mexico" --away "Canada"
python main.py update --home "Mexico" --away "Canada" --home-score 0 --away-score 5
python main.py finish --home "Mexico" --away "Canada"
python main.py summary
Testing
The library includes a set of unit tests to ensure its functionality. You can run the tests by executing the following command:

bash
Copy code
python -m unittest discover -s tests
License
This library is licensed under the MIT License.

Feel free to modify and use this library according to your needs.






