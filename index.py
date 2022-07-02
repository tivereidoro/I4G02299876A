
import random

print("\n\nWelcome.!! : \nRock-Paper-Scissors CLI game!!\n\n")

start_game = True

while start_game:
    # Take player input

    player_input = str(input(
        "Choose your character: \n\nEnter 'R' for Rock \nEnter 'P' for Paper \nEnter 'S' for Scissors\nEnter 'Z' to close game.\n"))
    # checks if it is an alphabet
    if not player_input.isalpha():
        print("This is not an alphabet\n\n")
        continue

    # convert player input to uppercase for uniformity
    player_choice = player_input.upper()

    if player_choice == "Z":
        print("Closed...")
        break

    # list for computer options
    computer_options = ["R", "P", "S"]

    # use inbuilt choice funtion from inbuilt python random module.
    computer_choice = random.choice(computer_options)

    print("You chose ", player_choice, " computer chose ", computer_choice)

    if player_choice == computer_choice:
        print("Both player chose ", player_choice, "It's a tie!")
    elif player_choice == "R":
        if computer_choice == "S":
            print("Rock smashes scissors! You win!\n\n")
        else:
            print("Paper covers rock! You lose.\n\n")
    elif player_choice == "P":
        if computer_choice == "R":
            print("Paper covers rock! You win!\n\n")
        else:
            print("Scissors cuts paper! You lose.\n\n")

    elif player_choice == "S":
        if computer_choice == "P":
            print("Scissors cuts paper! You win!\n\n")
        else:
            print("Rock smashes scissors! You lose.\n\n")
    else:
        print("Oops, ", player_choice,
              " is an Invalid input....Let's try that again\n\n")

    restart = input(
        "Will you like to play again?\n\nPress 'y' for yes or 'n' for no.")
    # Restart program
    if restart == "y":
        continue
    else:
        print("Thank you for playing.")
        break
