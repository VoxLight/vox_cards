import vox_cards.deck as cards
"""
Here is an example showing of the use of
the Suit enumerator defined as vox_cards.card.Suit.
I would like to note that the creation of suits
should be left to the card class in vox_cards.card.
Alls cards have a suit and value property, suit 
returns as a Suit enum and value is a number between
1 and 13 rating the cards values.
"""

deck = cards.Deck(1)

deck.shuffle()

deck.deal()

player = deck.hands[0]

for card in player:
    print(card.suit)
    # this will show the actual 
    # suit of the card in title case format
    # i.e. Spade or Hearts
    
print(player.cards[0].suit.value > player.cards[1].suit.value)
# kinda ugly, but since this isn't a practical use case it will have to do
# the main takeaway is that suit.value returns a number between 0 and 4
# 0 diamonds, 1 clubs, 2 hearts, 3 spades, 4 joker
# by comparing the value of a suit, you can tell if one suit is greater
# then another if you have to break ties between two cards with the same value
    
