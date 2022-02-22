"""Ex05: test use."""

__author__ = "730393353"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_use_fst() -> None:
    """Test only_evens case 1."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_use_snd() -> None:
    """Test only_evens case 2."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_sub_single() -> None:
    """Empty list with incorrect indices."""
    xs: list[int] = []
    a: int = -1
    b: int = 0
    assert sub(xs, a, b) == []


def test_sub_fst() -> None:
    """Test sub case 1."""
    xs: list[int] = [10, 20, 30, 40]
    a: int = 1
    b: int = 3
    assert sub(xs, a, b) == [20, 30]


def test_sub_snd() -> None:
    """Test sub case 2."""
    xs: list[int] = [37, 27, 17, 7, 0, -7]
    a: int = 3
    b: int = 4
    assert sub(xs, a, b) == [7]


def test_concat_empty() -> None:
    """Empty list."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_fst() -> None:
    """Test concat case 1."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_snd() -> None:
    """Test concat case 1."""
    xs: list[int] = [7, 17, 27, 37, -7]
    ys: list[int] = [-17]
    assert concat(xs, ys) == [7, 17, 27, 37, -7, -17]