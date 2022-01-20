"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730393353"

entered_word: str = input("Enter a 5-character word: ")
length_word: int = len(entered_word)
if length_word != 5:
    print("Error: Word must contain 5 characters")
    exit()

entered_char: str = input("Enter a single character: ")
length_char: int = len(entered_char)
if length_char != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + entered_char + " in " + entered_word)
number: int = 0

if entered_char == entered_word[0]:
    print(entered_char + " found at index 0")
    number = number + 1
if entered_char == entered_word[1]:
    print(entered_char + " found at index 1")
    number = number + 1
if entered_char == entered_word[2]:
    print(entered_char + " found at index 2")
    number = number + 1
if entered_char == entered_word[3]:
    print(entered_char + " found at index 3")
    number = number + 1
if entered_char == entered_word[4]:
    print(entered_char + " found at index 4")
    number = number + 1

    
if number == 0:
    print("No instances of " + entered_char + " found in heels")
else:
    print(str(number) + " instances of " + entered_char + " found in " + entered_word)