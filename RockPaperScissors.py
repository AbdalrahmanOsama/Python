import random


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_score = 0
        computer_score = 0
        start = input("Press ENTER to play or \"q\" to quit. ")
        if start == "q":
            print("GOODBYE :D")
            break
        elif not start:
            print("OK LET\'S PLAY! :D")
        else:
            print("Please Enter a Valid Reply.")
        while True:
            random_number = random.randint(0, 2)
            computer_choice = choices[random_number]
            user_choice = input("Choose:\n  0 Rock\n  1 Paper\n  2 Scissors\n")
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if 0 > user_choice > 2:
                    print("Please enter a valid choice.")
            else:
                print("Please enter a value.")
            user_choice = choices[user_choice]
            print(f"Computer Choice is {computer_choice}.")

            #winning conditions
            if user_choice == "rock" and computer_choice == "scissors":
                user_score += 1
                print(f"User Wins!\nUser Score: {user_score}\nComputer Score: {computer_score}")
            elif user_choice == "paper" and computer_choice == "rock":
                user_score += 1
                print(f"User Wins!\nUser Score: {user_score}\nComputer Score: {computer_score}")
            elif user_choice == "scissors" and computer_choice == "paper":
                user_score += 1
                print(f"User Wins!\nUser Score: {user_score}\nComputer Score: {computer_score}")
            #losing conditions
            elif user_choice == "rock" and computer_choice == "paper":
                computer_score += 1
                print(f"Computer Wins!\nUser Score: {user_score}\nComputer Score: {computer_score}")
            elif user_choice == "paper" and computer_choice == "scissors":
                computer_score += 1
                print(f"Computer Wins!\nUser Score: {user_score}\nComputer Score: {computer_score}")
            elif user_choice == "scissors" and computer_choice == "rock":
                computer_score += 1
                print(f"Computer Wins!\nUser Score: {user_score}\nComputer Score: {computer_score}")
            #draw conditions
            elif user_choice == "rock" and computer_choice == "rock":
                print(f"DRAW!\nUser Score: {user_score}\nComputer Score: {computer_score}")
            elif user_choice == "paper" and computer_choice == "paper":
                print(f"DRAW!\nUser Score: {user_score}\nComputer Score: {computer_score}")
            elif user_choice == "scissors" and computer_choice == "scissors":
                print(f"DRAW!\nUser Score: {user_score}\nComputer Score: {computer_score}")
            #score check
            if user_score == 3:
                print("The User is Winner!!")
                game = int(input("Do you want to play again?\n0 NO\n1 YES\n"))
                if game == 0:
                    quit()
                elif game == 1:
                    break
                else:
                    print("Enter a valid reply.")
                break
            elif computer_score == 3:
                print("The Computer is Winner!!")
                game = int(input("Do you want to play again?\n0 NO\n1 YES\n"))
                if game == 0:
                    print("GOODBYE :D")
                    quit()
                elif game == 1:
                    break
                else:
                    print("Enter a valid reply.")
                break
            else:
                continue


print("Welcome to Rock,Paper,Scissors Game!")
rock_paper_scissors()
