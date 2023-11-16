import random
  # Function to define the computer's move
def computer_move():
# Function to define the user's move
  def get_user_move():
    user_input = input("Enter 0 for rock, 1 for paper, 2 for scissors: ")
    # Check if the user's input is valid
    if user_input not in ['0', '1', '2']:
        print("Invalid input. Please enter a number 0, 1, or 2.")
        return None
    random.randint(0, 2)
    return int(user_input)
# Function to play the game
def play_game():
    user_move = get_user_move()
    if user_move is None:
        return
    # Define the computer's move
    comp_move = computer_move()
    # Determine the winner
    if user_move == comp_move:
        print("Draw!")
    elif (user_move == 0 and comp_move == 2) or \
       (user_move == 1 and comp_move == 0) or \
       (user_move == 2 and comp_move == 1):
        print("User wins!")
    else:
        print("Computer wins!")
# Play the game
play_game()