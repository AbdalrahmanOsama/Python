

def game():
    print("Welcome to Quiz Game!")
    play = input("Do you want to play (Y/N)? ").upper()
    if play == "N":
        print("BYE.")
        quit()
    elif play == "Y":
        print("OK! :D")
    else:
        print("Please Enter a valid reply.")
    

game()
