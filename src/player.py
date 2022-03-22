class Player:
    def __init__(self, is_dealer, credit):
        self.cards = []
        self.score = 0
        self.is_dealer = is_dealer
        self.credit = credit

    def _score(self):
        score = 0
        for card in self.cards:
            score += card.score()
            if card.score() == 11 and score > 10:
                score -= 10
        self.score = score
        return None

    def get_cards(self, cards):
        self.cards.extend(cards)
        self._score()
        return None

    def show_score(self):
        if self.is_dealer:
            print(f"Dealer cards: {self.cards}. Score: \033[1;33;10m{self.score}\033[1;33;0m")
        else:
            print(f"Player cards: {self.cards}. Score: \033[1;33;10m{self.score}\033[1;33;0m")
