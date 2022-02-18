"""Example of a function that searches through a list."""


def main() -> None:
    print(contains("D", ["A", "B"]))


# Define a funciton named contains
# Two parameters:
#  1. needle - the string we're searching for
#  2. haystack - the list we're searching through
def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm:
    #  For each item in the haystack
    #   Test if it is equal to the needles
    #       If so, return True
    for item in haystack:
        if item == needle:
            return True
#  After testing all items, return False, because not found
# Returns true if needle in heystack, false otherwise
    return False


if __name__ == "__main__":
    main()