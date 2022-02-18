"""Ex05: list utility functions."""

__author__ = "730393353"


# Name: only_evens
# Arguments: A list of integers.
# Returns: A list of integers, containing only the even elements of the input parameter.
def only_evens(xs: list[int]) -> list[int]:
    """Return the even numbers in the list."""
    new_xs: list[int] = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            new_xs.append(xs[i])
        i += 1
    return new_xs


# Name: sub
# Parameters: A list and two ints, where the first int serves as a start index and the second int serves as an end index (not inclusive).
# Returns: A List which is a subset of the given list, between the specified start index and the end index - 1.
def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Return elements in a list from index a to b-1."""
    new_list: list[int] = []
    if a < 0:
        a = 0
    if b > len(xs):
        b = len(xs)
    if len(xs) == 0 or a > len(xs) or b <= 0:
        return new_list
    while a < b:
        new_list.append(xs[a])
        a += 1
    return new_list


# Name: concat
# Parameters: Two lists of ints.
# Returns: A list containing all elements of the first list, followed by all elements of the second list.
def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatenate two lists."""
    a: int = len(xs)
    b: int = len(ys)
    i: int = 0
    new_list: list[int] = []
    while i < a:
        new_list.append(xs[i])
        i += 1
    i = 0
    while i < b:
        new_list.append(ys[i])
        i += 1
    return new_list