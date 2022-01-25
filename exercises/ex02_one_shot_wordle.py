"""Ex02 - One Shot."""
__author__ = "730393353"

secret: str = "python"
user_guess: str = input(f"What is your {len(secret)}-letter guess? ")
length_of_guess: int = len(user_guess)
while length_of_guess != len(secret):
    user_guess = input(f"That was not {len(secret)} letters! Try again: ")
    length_of_guess: int = len(user_guess)

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
i: int = 0
result_emoji: str = ""
while i < len(secret):
    if user_guess[i] == secret[i]:
        result_emoji = result_emoji + green_box
    else:
        if_exist: bool = user_guess[i] == secret[i]
        i_alt: int = 0
        while (if_exist == (not True)) and (i_alt < len(secret)):
            if user_guess[i] == secret[i_alt]:
                if_exist = True
            else:
                i_alt = i_alt + 1
        if if_exist:
            result_emoji = result_emoji + yellow_box
        else:
            result_emoji = result_emoji + white_box
    i = i + 1

print(result_emoji)
if user_guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")