import random

# Snake, Water, Gun Game Logic
def fungame(computer, player):
    # If both choices are the same, declare a tie
    if computer == player:
        return None

    # Game logic for Snake, Water, and Gun
    if computer == 's':
        return player == 'g'
    elif computer == 'w':
        return player == 's'
    elif computer == 'g':
        return player == 'w'

# Game Start
print("Welcome to the Snake, Water, Gun Game!")
print("Computer Turn: Snake(s), Water(w), or Gun(g)?")

# Random choice for the computer
randNo = random.randint(1, 3)
computer = 's' if randNo == 1 else 'w' if randNo == 2 else 'g'

# Player's choice
player = input("Your Turn: Snake(s), Water(w), or Gun(g)? ").lower()

# Validate input
if player not in ['s', 'w', 'g']:
    print("Invalid choice! Please choose 's', 'w', or 'g'.")
else:
    # Determine the result
    result = fungame(computer, player)

    # Display choices
    print(f"Computer chose: {computer}")
    print(f"You chose: {player}")

    # Display the result
    if result is None:
        print("The game is a tie!")
    elif result:
        print("You Win!")
    else:
        print("You Lose!")
