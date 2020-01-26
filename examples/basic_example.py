from vox_cards.deck import Deck

deck = cards.Deck(2) # Pass the number of hands to construct this deck with.

deck.deal() # The default number of cards to deal is 7

player_1, player_2 = deck.hands

for card in player_1: # Print all cards in the first hand.
	print(card.full) # Prints the full name of the card (i.e. "10 of Clubs").
