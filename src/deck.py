import random
from .card import Card


class Deck:
    def __init__(self):
        self.deck = []

    def create_deck(self):
        for i in range(1, 5):
            for j in range(1, 14):
                self.deck.append(Card(j, i))

    def draw(self, number_of_cards):
        cards = []
        for _ in range(number_of_cards):
            card = random.choice(self.deck)
            cards.append(card)
            self.deck.remove(card)
        return cards

    # def count(self):
    #     return len(self.deck)
