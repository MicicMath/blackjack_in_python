from .deck import Deck
from .player import Player

CRD_DEFAULT_STEP = 100.0
SCORE_21 = 21
SCORE_17 = 17


class Game:
    def __init__(self, credit):
        self.deck = Deck()
        self.deck.create_deck()
        self.player = Player(is_dealer=False, credit=credit)
        self.dealer = Player(is_dealer=True, credit=credit)

    def play(self):
        crd = input("Enter amount [100/custom]: ")
        if crd != "":
            crd = float(crd)
        else:
            crd = CRD_DEFAULT_STEP
        while crd > self.player.credit:
            crd = input(
                f"Amount {crd} too high. Tot. credit: {self.player.credit}. Enter new amount [MAX/custom]: "
            )
            if crd != "":
                crd = float(crd)
            if crd == "":
                crd = self.player.credit

        # self.player.credit -= crd
        print(f"Amount used: {crd}. Tot. credit remaining: {self.player.credit - crd}")
        print("------------------------------------------------")

        self.player.get_cards(self.deck.draw(2))
        self.dealer.get_cards(self.deck.draw(2))

        # check if inital scores = 21
        if self.player.score == SCORE_21:
            if self.dealer.score == SCORE_21:
                self.player.credit -= crd
                self.player.show_score()
                self.dealer.show_score()
                self.msg_player_lost()
                return None
            else:
                self.player.credit += crd
                self.player.show_score()
                self.dealer.show_score()
                self.msg_player_won()
                return None

        self.player.show_score()
        self.dealer.show_score()

        print("------------------------------------------------")
        ask = input("Deal [Y/n]? ")
        print("------------------------------------------------")
        while ask != "n":
            self.player.get_cards(self.deck.draw(1))
            self.player.show_score()
            if self.player.score == SCORE_21:
                break
            if self.player.score > SCORE_21:
                self.player.credit -= crd
                self.msg_player_lost()
                return None
            if self.dealer.score < SCORE_17:
                self.dealer.get_cards(self.deck.draw(1))
                self.dealer.show_score()
                if self.dealer.score > SCORE_21:
                    self.player.credit += crd
                    self.msg_player_won()
                    return None
                if self.dealer.score == SCORE_21:
                    self.player.credit -= crd
                    self.msg_player_lost()
                    return None
            if self.dealer.score >= 17 and self.player.score > self.dealer.score:
                break

            print("------------------------------------------------")
            ask = input("Deal [Y/n]? ")
            print("------------------------------------------------")

        while self.dealer.score < SCORE_17 and self.player.score > self.dealer.score:
            self.dealer.get_cards(self.deck.draw(1))
            self.dealer.show_score()
            if self.dealer.score > SCORE_21:
                self.player.credit += crd
                self.msg_player_won()
                return None
            if self.player.score <= self.dealer.score:
                self.player.credit -= crd
                self.msg_player_lost()
                return None

        if self.player.score > self.dealer.score:
            self.player.credit += crd
            self.msg_player_won()
            return None
        else:
            self.player.credit -= crd
            self.msg_player_lost()
            return None

    def msg_player_won(self):
        credit = self.player.credit
        print("------------------------------------------------")
        print(f"\033[1;37;10mPLAYER WON!\033[0;37;0m Tot. bank: {credit}")
        print("------------------------------------------------")

    def msg_player_lost(self):
        credit = self.player.credit
        print("------------------------------------------------")
        print(f"\033[1;37;10mPLAYER LOST!\033[0;37;0m Tot. bank: {credit}")
        print("------------------------------------------------")
