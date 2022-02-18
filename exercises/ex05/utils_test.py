"""Ex05: test use."""

__author__ = "730393353"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_use_fst() -> None:
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_use_snd() -> None:
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_sub_empty() -> None:
    xs: list[int] = []
    a: int = 0
    b: int = 0
    assert sub(xs, a, b) == []


def test_sub_fst() -> None:
    xs: list[int] = [10, 20, 30, 40]
    a: int = 1
    b: int = 3
    assert sub(xs, a, b) == [20, 30]


def test_sub_snd() -> None:
    xs: list[int] = [37, 27, 17, 7, 0, -7]
    a: int = 3
    b: int = 4
    assert sub(xs, a, b) == [7]


def test_concat_empty() -> None:
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_fst() -> None:
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_snd() -> None:
    xs: list[int] = [7, 17, 27, 37, -7]
    ys: list[int] = [-17]
    assert concat(xs, ys) == [7, 17, 27, 37, -7, -17]