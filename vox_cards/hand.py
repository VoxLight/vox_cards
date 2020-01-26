# builtins
import random

# locals
from .card import Card

class Hand:
    def __init__(self, deck):
        self.cards = []
        self.deck = deck

        # properties
        self._card_count = len(self.cards)
    
    def __iter__(self):
        return iter(self.cards)

    @property
    def card_count(self):
        self._card_count = len(self.cards)
        return self._card_count

    def discard(self, to_discard=1):
        if type(to_discard) == int:
            if to_discard == self.card_count:
                self.deck.discarded_cards += self.cards
                self.cards = []
            else:
                for _ in range(to_discard):
                    self.deck.discarded_cards.append(
                        self.cards.pop(
                            random.randint(0, len(self.cards)-1)
                        )
                    )
        elif type(to_discard) == Card:
            try:
                self.deck.discarded_cards.append(
                    self.cards.pop(
                        self.cards.index(to_discard)
                    )
                )
            except ValueError as e:
                print(e)



    def draw(self, amount=1):
        """
        Refer to deck.deal docstring

        Simulates drawing from the top of
        the deck, rather than pulling a random card.
        """
        cards = []
        for _ in range(amount):
            card = self.deck.cards.pop()
            self.deck.drawn_cards.append(card)
            self.cards.append(card)
            cards.append(card)
        return cards
