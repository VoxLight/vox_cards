# builtins
from enum import Enum
import json

class Suit(Enum):
    """An Enumeration to make handling card suits easier.

    :param suit: A number between 0 and 4 denoting the suit, they are diamonds, clubs, hearts, spades, and joker respectively.
    :type Int: class:`int`
    :return: Returns an enum representing the suit. str(Suit) returns the titlecase representation of the suit name.
    :rtype: class:`enum.Enum`
    """


    DIAMONDS = 0
    CLUBS = 1
    HEARTS = 2
    SPADES = 3
    JOKER = 4

    def __str__(self):
        return self.name.title()
        


class Card:
    """[Summary]

    :param card_data: A dictionary with a suit and value.
    :type dict: class:`dict`
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]
    """
    def __init__(self, card_data):
        """Constructor method
        """
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
        
