import random
playerChoice = input("rock, paper, or scissors? \n")
choices = ['rock', 'paper', 'scissors']
compChoice = random.choice(choices)

if compChoice == playerChoice:
    print(f"It's a tie!  You both chose {compChoice}.  Try again?")

elif (
    (compChoice == 'rock' and playerChoice == 'scissors') or 
    (compChoice == 'paper' and playerChoice == 'rock') or
    (compChoice == 'scissors' and playerChoice == 'paper')
    ):
    print(f"You lost! {compChoice} beats {playerChoice}. Try again?")

elif (
    (playerChoice == 'rock') or 
    (playerChoice == 'paper') or 
    (playerChoice == 'scissors')
    ):
    print(f"You won! {playerChoice} beats {compChoice}.")

else:
    print("\nPlease enter a valid choice!")