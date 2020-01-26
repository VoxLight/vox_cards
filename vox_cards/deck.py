# builtins
import random
import json

# locals
from .card import Card
from .hand import Hand



class Deck:
    with open("./deck_data.json", "r") as data:
        deck_data = json.load(data)

    default_deck = [Card(d) for d in deck_data["cards"]]

    def __init__(self, hands=1, jokers=False):
        self.cards = Deck.default_deck 
        self.hands = [Hand(self) for _ in range(hands)] 
        self.drawn_cards = []
        self.discarded_cards = []
        self.is_shuffled = False

        

    def deal(self, amount=1):
        """
        This method of dealing is superior to drawing
        x amount of random.choice(deck) because it
        keeps the deck in a static order. It simulates
        having a shuffled deck and dealing from the top
        to each of the players (hands).
        """
        for _ in range(amount):
            for hand in self.hands:
                hand.draw(self)

    def shuffle(self, new_deck=False, new_hands=True):
        if new_hands:
            for hand in self.hands:
                hand.discard(hand.card_count)
            self.cards += self.discarded_cards
            
        if new_deck:
            self.discarded_cards = []
            self.drawn_cards = []
            self.cards = Deck.default_deck
        

        cut1, cut2 = self.cards[:len(self.cards)//2], self.cards[len(self.cards)//2:]
        self.cards = []
        for _ in range(len(self.cards)//2):
            self.cards.append(cut1.pop(cut1.index(random.choice(cut1))))
            self.cards.append(cut2.pop(cut2.index(random.choice(cut2))))

    def __iter__(self):
        return self.cards
            