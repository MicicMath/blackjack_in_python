# Simple blackjack in python

Simple two player (player vs. dealer) blackjack in python played in terminal. Python 3.x required.

Game play:
- Rules as in blackjack.
- Player starts. Player has credit of 500. When credit reaches 0 game ends.
- Dealer takes cards up to max. score of 17.  

Run: 
```bash
python run_game.py
```

All classes are in ```src``` folder. Classes defined:
- Card class (```card.py```): defines card and value of the card.
- Deck class (```deck.py```): creates a deck and draws from deck.
- Player class (```player.py```): defines a player (player or dealer). Player can get cards and has score associated with the cards. 
- Game class (```game.py```): creates a game instance. Game logic is in the "play" method.


