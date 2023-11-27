import random


# Function to determine the winner for a single round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "You win this round!", 1
    else:
        return "You lose this round!", -1


# Function to print a border
def print_border():
    print("+" + "-" * 50 + "+")


# Main function to play the game
def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print_border()
    print("|{:^50}|".format("Welcome to Rock, Paper, Scissors Game!"))
    print_border()

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()

        if user_choice == 'q':
            break

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.\n")
            continue

        computer_choice = random.choice(choices)
        print_border()
        print("|{:<50}|".format("You chose: " + user_choice))
        print("|{:<50}|".format("Computer chose: " + computer_choice))

        result, score = determine_winner(user_choice, computer_choice)
        print("|{:<50}|".format(result))

        if score == 1:
            user_score += 1
        elif score == -1:
            computer_score += 1

        print("|{:<25} You:{:^5}{:^11}Computer:{:^4}|".format("Current Score -", user_score, "", computer_score))
        print_border()

    print("\nThank you for playing!")
    print("Final scores - You:", user_score, ", Computer:", computer_score)


if __name__ == "__main__":
    play_game()
