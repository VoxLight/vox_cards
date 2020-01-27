.. highlight:: python

Examples
========


Basic Usage Cont.
+++++++++++++++++

.. code-block:: py
    :linenos:

    import vox_cards.deck as cards

    deck = cards.Deck(2) 
    # Pass the number of hands to construct this deck with.

    deck.deal() # The default number of cards to deal is 7

    player_1, player_2 = deck.hands

    for card in player_1: # Print all cards in the first hand.
        print(card.full) 
        # Prints the full name of the card (i.e. "10 of Clubs").

Keep in mind that hands are iterable, but only return the cards they hold. 
With that in mind, there is also the ability for hands to draw and discard cards.

.. code-block:: py
    :linenos:
    :lineno-start: 13

    # This will draw the top 2 cards for each palyer, then discard 2 cards at random.
    player_1.draw(2)
    player_1.discard(2)

    player_2.draw(2)
    player_2.discard(2)


    # You can also pass a card instance to hand.discard for discarding specific card(s).
    player_1.discard(player_1.cards[0])
    player_2.discard(player_2.cards[0])


Poker
+++++

This is poker... kind of. It should give you the general idea of how hands
work as a "player", and the instances created by the deck can act as the 
players who are playing the card game, and an AI dealer aswell. Or you could
give control of the dealer hand to a player and let them be the dealer. You pick.

.. code-block:: py
    :linenos:

    import vox_cards.deck as cards

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


