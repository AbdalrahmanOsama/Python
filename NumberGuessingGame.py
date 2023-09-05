import random


def number_guessing_game():
    while True:
        play = input("Press ENTER to play or \"q\" to quit. ")
        if play == "q":
            break
        elif not play:
            print("OK LET\'S PLAY! :D")
        else:
            print("Please Enter a Valid Reply.")
        top_of_range = input("Enter the top of the range: ")
        if top_of_range.isdigit():
            top_of_range = int(top_of_range)
            if top_of_range <= 0:
                print("Please enter a range greater than zero.")
        else:
            print("Please enter a value.")
        RANDOM_NUMBER = random.randint(0, top_of_range)
        guesses = 1
        while True:
            answer = input("Try to guess the number :P ")
            if answer.isdigit():
                answer = int(answer)
                if answer < 0:
                    print("Amount must be greater than zero.")
            else:
                print("Please enter a valid number.")
            if answer == RANDOM_NUMBER:
                print(f"Right Guess!\nYou got it in {guesses} guesses.")
                break
            elif answer > RANDOM_NUMBER:
                print("Try again.")
                guesses += 1
                print("HINT: You are above the number ;)")
            else:
                print("Try again.")
                guesses += 1
                print("HINT: You are below the number ;)")
            continue


print("Welcome to GuessTheNumber Game!")
number_guessing_game()
