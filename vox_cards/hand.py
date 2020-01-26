class Hand:
    def __init__(self, cards=[]):
        self.cards = cards

        # properties
        self._hand_count = len(cards)
    
    def __iter__(self):
        return self.cards

    @property
    def hand_count(self):
        self._hand_count = len(self.cards)
        return self._hand_count

    def draw(self, deck):
        """
        Refer to deck.deal docstring

        Simulates drawing from the top of
        the deck, rather than pulling a random card.
        """
        card = deck.pop()
        self.cards.append(card)
        return card
