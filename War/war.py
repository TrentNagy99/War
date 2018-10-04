# War
# A player competed against the dealer.
# Whoever draws the highest value card wins.

import cards
import games


class War_Card(cards.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        v = War_Card.RANKS.index(self.rank) + 1
        if v == "J":
            v = 11
        elif v == "Q":
            v = 12
        elif v == "K":
            v = 13
        return v


class War_Deck(cards.Deck):
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.cards.append(War_Card(rank, suit))


class War_Hand(cards.Hand):
    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(War_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        t = 0
        for card in self.cards:
            t += card.value
        return t


class War_Player(War_Hand):
    def win(self):
        print(self.name, "wins")


class War_Dealer(War_Hand):
    def win(self):
        print("Dealer wins")


class War_Game(object):
    def play(self, names):
        self.players = []

        player = War_Player(names)
        self.players.append(player)

        self.dealer = War_Dealer("Dealer")

        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.deck.deal(self.players + [self.dealer], per_hand=1)

        print(self.players[0])
        print(self.dealer)

        if player.total > self.dealer.total:
            player.win()
        elif player.total < self.dealer.total:
            self.dealer.win()
        else:
            print("It was a tie!")


def main():
    print("Welcome to War!")

    name = input("Enter the player name: ")

    game = War_Game()

    again = None
    while again != "n":
        game.play(name)
        again = games.ask_yes_no("\nDo you want to play again?")


main()
input("\n\nPress enter to continue.")