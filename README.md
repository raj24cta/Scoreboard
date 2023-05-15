To start a new match:


python main.py start --home "Mexico" --away "Canada"

To update the scores of a match:


python main.py update --home "Mexico" --away "Canada" --home-score 0 --away-score 5

To finish a match:


python main.py finish --home "Mexico" --away "Canada"

To get a summary of ongoing matches:


python main.py summary

Additionally, the library includes unit tests to ensure its functionality. You can run these tests by executing the following command:


      python -m unittest discover -s tests





