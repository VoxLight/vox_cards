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
        self.value = card_data["value"]
        self.suit = Suit(card_data["suit"])
        if self.value == 0:
            self.text = "Joker"
        elif self.value == 1:
            self.text == "Ace"
        elif self.value == 11:
            self.text == "Jack"
        elif self.value == 12:
            self.text == "Queen"
        elif self.value == 13:
            self.text == "King"
        else:
            self.text = str(self.value)
        self.full = f"{self.text} of {str(self.suit)}"



if __name__ == "__main__":
    with open("./deck_data_new.json", 'r') as f:
        deck_data = json.load(f)
    
    cards = [Card(card) for card in deck_data["cards"]]

    for card in cards:
        print(str(card.suit))

