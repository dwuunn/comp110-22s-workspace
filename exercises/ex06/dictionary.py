"""Ex06 - Dictionary Functions."""

__author__ = "730393353"


def invert(pos: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in the dictionary pos."""
    neg: dict[str, str] = {}
    for key in pos:
        if pos[key] in neg:
            raise KeyError
        neg[pos[key]] = key
    return neg


def favorite_color(nacol: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    count_color: dict[str, int] = {}
    for key in nacol:
        i: int = 1
        if nacol[key] in count_color:
            count_color[nacol[key]] = i + 1
        else:
            count_color[nacol[key]] = i
    max: str = ""
    ii: int = 0
    for keyy in count_color:
        if count_color[keyy] > ii:
            max = keyy
            ii = count_color[keyy]
    return max


def count(alist: list[str]) -> dict[str, int]:
    """Count the number of times each value appears in the input list."""
    count_color: dict[str, int] = {}
    i: int = 1
    for item in alist:
        if item in count_color:
            count_color[item] += 1

        else:
            count_color[item] = i
    return count_color