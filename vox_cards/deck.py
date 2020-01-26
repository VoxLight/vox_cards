# builtins
import random
import json
import os

# locals
from .card import Card
from .hand import Hand

CARD_DATA = {
    "cards": [
        {"suit": 2, "value": 2}, 
        {"suit": 2, "value": 3}, 
        {"suit": 2, "value": 4}, 
        {"suit": 2, "value": 5}, 
        {"suit": 2, "value": 6}, 
        {"suit": 2, "value": 7}, 
        {"suit": 2, "value": 8}, 
        {"suit": 2, "value": 9}, 
        {"suit": 2, "value": 10}, 
        {"suit": 2, "value": 11}, 
        {"suit": 2, "value": 12}, 
        {"suit": 2, "value": 13}, 
        {"suit": 2, "value": 1}, 
        {"suit": 0, "value": 2}, 
        {"suit": 0, "value": 3}, 
        {"suit": 0, "value": 4}, 
        {"suit": 0, "value": 5}, 
        {"suit": 0, "value": 6}, 
        {"suit": 0, "value": 7}, 
        {"suit": 0, "value": 8}, 
        {"suit": 0, "value": 9}, 
        {"suit": 0, "value": 10}, 
        {"suit": 0, "value": 11}, 
        {"suit": 0, "value": 12}, 
        {"suit": 0, "value": 13}, 
        {"suit": 0, "value": 1}, 
        {"suit": 1, "value": 2}, 
        {"suit": 1, "value": 3}, 
        {"suit": 1, "value": 4}, 
        {"suit": 1, "value": 5}, 
        {"suit": 1, "value": 6}, 
        {"suit": 1, "value": 7}, 
        {"suit": 1, "value": 8}, 
        {"suit": 1, "value": 9}, 
        {"suit": 1, "value": 10}, 
        {"suit": 1, "value": 11}, 
        {"suit": 1, "value": 12}, 
        {"suit": 1, "value": 13}, 
        {"suit": 1, "value": 1}, 
        {"suit": 3, "value": 2}, 
        {"suit": 3, "value": 3}, 
        {"suit": 3, "value": 4}, 
        {"suit": 3, "value": 5}, 
        {"suit": 3, "value": 6}, 
        {"suit": 3, "value": 7}, 
        {"suit": 3, "value": 8}, 
        {"suit": 3, "value": 9}, 
        {"suit": 3, "value": 10}, 
        {"suit": 3, "value": 11}, 
        {"suit": 3, "value": 12}, 
        {"suit": 3, "value": 13}, 
        {"suit": 3, "value": 1}
    ], 
    "joker": [
        {"suit": 4, "value": 0}
    ]
}




class Deck:
    deck_data = CARD_DATA

    default_deck = [Card(d) for d in deck_data["cards"]]
    joker = Card(deck_data["joker"])

    def __init__(self, hands=1, jokers=False):
        self.cards = Deck.default_deck
        if jokers:
            self.cards += [Deck.joker]*2
        self.hands = [Hand(self) for _ in range(hands)] 
        self.drawn_cards = []
        self.discarded_cards = []
        self.is_shuffled = False

        

    def deal(self, amount=7):
        """
        This method of dealing is superior to drawing
        x amount of random.choice(deck) because it
        keeps the deck in a static order. It simulates
        having a shuffled deck and dealing from the top
        to each of the players (hands).
        """
        for _ in range(amount):
            for hand in self.hands:
                hand.draw()

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
        return iter(self.cards)
            