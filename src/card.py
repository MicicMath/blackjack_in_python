FACES = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
SUITS_UNICODE = ["\u2663", "\u2660", "\u2666", "\u2665"]


class Card:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = FACES[row - 1]
        self.suit = SUITS_UNICODE[col - 1]

    def score(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        if self.value == 'A':
            return 11
        return self.value

    def show(self):
        num = self.value
        suit = self.suit
        val = self.score()
        return f"({suit}{num}) = {val}"

    def __repr__(self):
        return f"\033[1;33;10m{self.suit}{self.value}\033[1;33;0m"
