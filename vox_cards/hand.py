# builtins
import random

# locals
from .card import Card

class Hand:
    def __init__(self, deck, cards=[]):
        self.cards = cards
        self.deck = deck

        # properties
        self._hand_count = len(cards)
    
    def __iter__(self):
        return iter(self.cards)

    @property
    def card_count(self):
        self._hand_count = len(self.cards)
        return self._hand_count

    def discard(self, to_discard=1):
        if type(to_discard) == int:
            if to_discard == self.hand_count:
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
            self.deck.discarded_cards.append(
                self.cards.pop(
                    self.cards.index(to_discard)
                )
            )



    def draw(self, deck):
        """
        Refer to deck.deal docstring

        Simulates drawing from the top of
        the deck, rather than pulling a random card.
        """
        card = deck.cards.pop()
        self.deck.drawn_cards.append(card)
        self.cards.append(card)
        return card
