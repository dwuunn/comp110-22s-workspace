"""Ex06: test use."""

__author__ = "730393353"


from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Empty dictionary."""
    dzero: dict[str, str] = {}
    assert invert(dzero) == {}


def test_invert_one() -> None:
    """Test invert case 1."""
    done: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(done) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_two() -> None:
    """Test invert case 2."""
    dtwo: dict[str, str] = {'Galileo': 'telescope', 'Kepler': 'orbit', 'Newton': 'gravitational laws'}
    assert invert(dtwo) == {'telescope': 'Galileo', 'orbit': 'Kepler', 'gravitational laws': 'Newton'}


def test_favorite_color_empty() -> None:
    """Empty dictionary."""
    dzero: dict[str, str] = {}
    assert favorite_color(dzero) == ""


def test_favorite_color_tie() -> None:
    """There is a tie for most popular color."""
    dtie: dict[str, str] = {'a': 'blue', 'b': 'pink'}
    assert favorite_color(dtie) == 'blue'


def test_favorite_color_use() -> None:
    """When there is a color that appears most frequently."""
    duse: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(duse) == 'blue'


def test_count_empty() -> None:
    """Empty list."""
    lempty: list[str] = []
    assert count(lempty) == {}


def test_count_one() -> None:
    """Case one."""
    lone: list[str] = ["arth"]
    assert count(lone) == {"arth": 1}


def test_count_two() -> None:
    """Case two."""
    ltwo: list[str] = ["arth", "econ", "astr", "arth", "astr"]
    assert count(ltwo) == {"arth": 2, "astr": 2, "econ": 1}