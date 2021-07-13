# import necessary module
import random

while True :
    # choices
    Rock = 1
    Paper = 2
    Scissors = 3

    # variable definitions
    player_choice = int(input("Enter an option: Rock(1), Paper(2) or Scissors(3) : "))
    computer_choices = [1, 2, 3]
    computer_action = random.choice(computer_choices)

    # ask player to imput their choice
    def get_user_selection() :
        return player_choice

    get_user_selection()

    # determine the computers choice
    def get_computer_selection() :
        return computer_action

    get_computer_selection()

    # print out the chosen options
    print("You chose " , player_choice)
    print("The computer chose " , computer_action)

    # determine a winner
    def get_a_winner() :
        if player_choice == computer_action :
            print("It's a tie!")
        elif player_choice == 1 :
            if computer_action == 3 :
                print("You win")
            else : print("You lose")
        elif player_choice == 2 :
            if computer_action == 1 :
                print("You win")
            else : print("You lose")
        elif player_choice == 3 :
            if computer_action == 2 :
                print ("You win")
            else : print("You lose")

    get_a_winner()

    # play again or not?
    # def play_again() :
    play_again = input("Would you like to play again? Y/N: ")
    if play_again.lower() != "y" :
        print("Thanks for playing! Press Ctrl+C to exit the game")

    # play_again()
