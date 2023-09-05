exit_word = "chupacabra"

input_word = input("Enter a word: ")
while True:
    if input_word != exit_word:
        input_word = input("Enter a word: ")
    else:
        break
print("You've successfully left the loop.")

