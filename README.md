# Vox Cards
This is an easy to use dependancy free deck manager, making it easy to develope the logic of
card games without worrying about creating ways to handle the decks, cards, and hands.

### Installation
Install using pip:
`py -m pip install vox_cards`

### Usage
```Python
import vox_cards as cards

deck = cards.Deck(2) # Pass the number of hands to construct this deck with.

deck.deal() # The default number of cards to deal is 7

for card in deck.hands[0]:
    print(card.text)
```