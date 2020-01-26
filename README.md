# Vox Cards
This is an easy to use dependancy free deck manager, making it easy to develope the logic of
card games without worrying about creating ways to handle the decks, cards, and hands.

### Installation
Install using pip:
`py -m pip install vox_cards`

### Usage
```Python
from vox_cards.deck import Deck

deck = cards.Deck(2) # Pass the number of hands to construct this deck with.

deck.deal() # The default number of cards to deal is 7

player_1, player_2 = deck.hands

for card in player_1: # Print all cards in the first hand.
    print(card.full) # Prints the full name of the card (i.e. "10 of Clubs").
```
Keep in mind that hands are iterable, but only return the cards they hold.
With that in mind, there is also the ability for hands to draw and discard cards.
```Python
# This will draw the top 2 cards for each palyer, then discard 2 cards at random.
player_1.draw(2)
player_1.discard(2)

player_2.draw(2)
player_2.discard(2)


# You can also pass a card instance to hand.discard for discarding specific card(s).
player_1.discard(player_1[0])
player_2.discard(player_2[0])
```