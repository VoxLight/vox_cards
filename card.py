class Card:
    def __init__(self, card_data):
        self._data = card_data
        # from __getattr__
        # self.value
        # self.suit

    def __getattr__(self, value):
        return self._data[value]