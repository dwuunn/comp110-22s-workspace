"""Ex03 - wordle."""
__author__ = "730393353"


def contains_char(anylength: str, singlechar: str) -> bool:
    """Whether anylength contains singlechar at any index."""
    assert len(singlechar) == 1
    i: int = 0
    if_exist: bool = singlechar == anylength[i]
    while i < len(anylength) and (if_exist == (not True)):
        if singlechar == anylength[i]:
            if_exist = True
        else:
            i = i + 1
    if if_exist:
        return True
    else:
        return False


def emojified(guess_emo: str, secret_emo: str) -> str:
    """Return emoji result of the matching of guess and secret."""
    assert len(guess_emo) == len(secret_emo)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    i_alt: int = 0
    resulted_emoji: str = ""
    while i_alt < len(secret_emo):
        if not contains_char(secret_emo, guess_emo[i_alt]):
            resulted_emoji = resulted_emoji + white_box
        elif secret_emo[i_alt] == guess_emo[i_alt]:
            resulted_emoji = resulted_emoji + green_box
        else:
            resulted_emoji = resulted_emoji + yellow_box
        i_alt = i_alt + 1
    return resulted_emoji


def input_guess(length_of_secret: int) -> str:
    """Whether user's guess has the right length."""
    user_guess: str = input(f"Enter a {str(length_of_secret)} character word: ")
    while len(user_guess) != length_of_secret:
        user_guess = input(f"That wasn't {str(length_of_secret)} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    guess: str = ""
    result: str
    i_turn: int = 1
    while i_turn <= 6 and guess != secret:
        print(f"=== Turn {str(i_turn)}/6 ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)
        i_turn = i_turn + 1
    print(f"You won in {str(i_turn-1)}/6 turns!")
    if i_turn > 6:
        print("X/6 - Sorry, try again tomorrow!")
