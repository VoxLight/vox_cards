# builtins
import random
import json
import os

# locals
from .card import Card
from .hand import Hand

def generate_card_data():
    suits = 3
    values = 13
    cur_suit = 0
    cur_value = 1
    while cur_suit <= suits and cur_value <= values:
        yield {"suit":cur_suit, "value":cur_value}
        if cur_value == values:
            cur_suit += 1
            cur_value = 0
        cur_value += 1
        

JOKER = {"suit": 4, "value": 0}




class Deck:

    default_deck = [Card(d) for d in generate_card_data()]
    joker = Card(JOKER)

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
        
        cards = list(self.cards)
        random.shuffle(cards)
        self.cards = cards

    def __iter__(self):
        return iter(self.cards)
            