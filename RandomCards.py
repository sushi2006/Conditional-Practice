import random

# Function to simulate picking a card from a deck of 52 cards
def pick_card():
    # Define the ranks
    ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    # Define the suits
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    # Pick a random rank and suit
    rank = random.choice(ranks)
    suit = random.choice(suits)

    # Return the rank and suit of the card
    return rank, suit

# Play the game
while True:
    # Pick a card from the deck
    rank, suit = pick_card()

    # Display the rank and suit of the card
    print(f"You picked the {rank} of {suit}.")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")

    # If the user doesn't want to play again, break out of the loop
    if play_again.lower() != 'yes':
        break