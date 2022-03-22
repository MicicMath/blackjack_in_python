from src.game import Game

CREDIT = 500

if __name__ == "__main__":

    print("")
    print("-------------Blackjack in Python(3)-------------")
    print("Two player game: player vs. dealer. Player starts.")
    print(f"Player's starting credit: {CREDIT}")
    print("------------------------------------------------")

    game_status = True

    while game_status:
        game = Game(CREDIT)
        game.play()
        credit = game.player.credit
        if credit <= 0.0:
            print("Game over!")
            break
        ask = input("Continue? [Y/n]: ")
        print("------------------------------------------------")
        if ask != "n":
            game_status = True
        else:
            print("Game over")
            print("------------------------------------------------")
            game_status = False
