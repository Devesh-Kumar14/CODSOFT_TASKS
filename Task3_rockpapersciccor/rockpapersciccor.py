# Rock Paper Scissors Game

import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0


while True:

    print("\n==========================")
    print("   ROCK PAPER SCISSORS")
    print("==========================")

    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("\nEnter your choice: ").lower()

    # Convert number input to choice
    if user_choice == "1":
        user_choice = "rock"

    elif user_choice == "2":
        user_choice = "paper"

    elif user_choice == "3":
        user_choice = "scissors"

    elif user_choice not in choices:
        print("Invalid choice!")
        continue

    # Computer chooses randomly
    computer_choice = random.choice(choices)

    print("\nYour choice:", user_choice)
    print("Computer choice:", computer_choice)

    # Determine winner
    if user_choice == computer_choice:
        print("\nIt's a TIE!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("\nYou WIN!")
        user_score += 1

    else:
        print("\nYou LOSE!")
        computer_score += 1

    # Display score
    print("\n------ SCORE ------")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        print("Final Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        break