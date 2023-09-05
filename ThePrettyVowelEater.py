# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ").upper()
word_without_vowel = ""

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        word_without_vowel = word_without_vowel + letter

print(word_without_vowel)

