# builtins
from enum import Enum
import json

class Suit(Enum):
    DIAMONDS = 0
    CLUBS = 1
    HEARTS = 2
    SPADES = 3
    JOKER = 4

    def __str__(self):
        return self.name.title()
        


class Card:
    def __init__(self, card_data):
        self._data = card_data
        self.value = self._data["value"]
        self.suit = Suit(self._data["suit"])
        if self.value == 0:
            self.text = "Joker"
        elif self.value == 1:
            self.text = "Ace"
        elif self.value == 11:
            self.text = "Jack"
        elif self.value == 12:
            self.text = "Queen"
        elif self.value == 13:
            self.text = "King"
        else:
            self.text = str(self.value)
        self.full = f"{self.text} of {str(self.suit)}"
        
