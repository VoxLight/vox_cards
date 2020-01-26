import vox_cards.deck as cards
'''
Would you look at this?
It's pokwer - but without any logic!
This is the same script found on the
readme of this repo. Place your bets
for who will win this time after
player 2's crushing victory on
player 1.
'''

deck = cards.Deck(3) # Create a deck with 3 hands

for _ in range(3):
    deck.shuffle()
    # shuffle the deck 3 times - ultra realism

player_1, player_2, river = deck.hands # create a player 1, 2, and a river out of the hands

for _ in range(2): # deal 2 cards to each player, alternating.
    player_1.draw()
    player_2.draw()
    
river.draw(3) # draw 3 cards on the river
river.draw() # another
river.draw() # and we have them all, lets see who won.

print("\nPlayer 1's hand:")
for card in player_1:
    print(card.full) # heres player 1's cards
    
print("\nPlayer 2's hand:")
for card in player_2:
    print(card.full) # and player 2's cards
    
print("\n\nAnd the river is:")
for card in river:
    print(card.full) # and the winner is?