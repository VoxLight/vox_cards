# builtins
import random
import json

# locals
from ..card import Card
from ..hand import Hand



class Deck:
    with open("./deck_data.json", "r") as data:
        deck_data = json.load(data)

    default_deck = [Card(d) for d in deck_data["cards"]]

    def __init__(self, hands=1, jokers=False):
        self.cards = [] # TODO: fill with instances of Card
        self.hands = [Hand() for _ in range(hands)] # TODO: fill with instances of Hand
        self.is_shuffled = False
        

    def deal(self, amount=1):
        for i in range(amount):
            for hand in self.hands:
                hand.draw(self)

    def shuffle(self, new_deck=False, new_hands=True):
        if new_deck:
            if new_hands:
                for hand in self.hands:
                    hand.discard(hand.card_count)
        cut1, cut2 = self.cards[:len(self.cards)//2], self.cards[len(self.cards)//2:]
        self.cards = []
        for i in range(len(self.cards)//2):
            self.cards.append(cut1.pop(cut1.index(random.choice(cut1))))
            self.cards.append(cut2.pop(cut2.index(random.choice(cut2))))

    def __iter__(self):
        return self.cards
            