import sys

def intro():
    print("welcome to trasure Island!")
    print("You have to find a hidden treasure")

def make_choice(prompt, valid_options):
    """ helper function to handle input properly. Using the stripping
    and lower casing of input to prevent crashing"""
    while True:
        choice = input(prompt).lower().strip()
        if choice in valid_options:
            return choice
        else:
            print(f"Invalid! Please choose from the options: {','.join(valid_options)}")


def game_play():
    intro()

    choice_1 = make_choice("Do you want to go left or right?  ", ['left', 'right']) 

    if choice_1 == 'right':
        print("You are trapped in a quick sand! game over")
        return

    else:
        print("yay! you are in front of a misty lake. There is a beautiful island in the center")

        choice_2 = make_choice("Do you want to take a boat or enjoy a swim to cross it  ",
                               ['boat', 'swim'])
        if choice_2 == "swim":
            print("You are attacked by crocodiles. Game over!")
            return
        print("You safely reach the island")

        choice_3 = make_choice("Which door looks nice to you 'red', 'green', 'blue'  ", ['red', 'green', 'blue'])
        if choice_3 == 'red':
            print("oh no! Room filled with fire. Better luck next time ")

        elif choice_3 == 'green':
            print("Be alert! Lots of snake! Game over")

        elif choice_3 == "blue":
            print("Congratulations! The hidden trasures is yours.")


if __name__ == '__main__':
    while True:
        game_play()
        play_again = make_choice("\n Would you like to play again? 'yes' or 'no'", ["yes", "no"])

        if play_again == 'no':
            print("Thanks for playing!")
            sys.exit()









        
