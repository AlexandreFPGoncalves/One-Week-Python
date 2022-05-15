from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    computerMove = "rock"
elif num == 2:
    computerMove = "paper"
else:
    computerMove = "scissors"

# Ask a user to enter their move
usersMove = input("Please pick your move: ").lower()


# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("Your Move:")
if usersMove == "rock":
    print(rock)
elif usersMove == "paper":
    print(paper)
else: 
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("Computer's Move:")
if computerMove == "rock":
    print(rock)
elif computerMove == "paper":
    print(paper)
else: 
    print(scissors)

# Figure out who wins and print the result!

if usersMove == computerMove:
    print("It's a tie!")
elif usersMove == "rock" and computerMove == "scissors":
    print("You win!")
elif usersMove == "paper" and computerMove == "rock":
    print("You win!")
elif usersMove == "scissors" and computerMove == "paper":
    print("You win!")
else:
    print("You lose!")