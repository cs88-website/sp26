from typing import Iterator  # "t: Iterator[int]" means t is an iterator that yields integers

def count_occurrences(t: Iterator[int], n: int, x: int) -> int:
    """Return the number of times that x is equal to one of the
    first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(t, 3, 10)
    2
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(u, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(u, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(u)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(v, 6, 6)
    2
    """
    count = 0
    for _ in range(n):
        if next(t) == x:
            count += 1
    return count


def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    Traceback (most recent call last):
        ...
    ValueError: It's a trap!
    >>> list(trap(range(5), 5))
    Traceback (most recent call last):
        ...
    ValueError: It's a trap!
    >>> t2 = trap(map(abs, reversed(range(-6, -4))), 2)
    >>> next(t2)
    5
    >>> next(t2)
    6
    >>> next(t2)
    Traceback (most recent call last):
        ...
    ValueError: It's a trap!
    >>> t3 = trap([1, 5, 6, 7, 10], 3)
    >>> next(t3)
    1
    >>> next(t3)
    5
    >>> next(t3)
    6
    >>> next(t3)
    Traceback (most recent call last):
        ...
    ValueError: It's a trap!
    """
    t = iter(s)
    for _ in range(k):
        yield next(t)
    raise ValueError("It's a trap!")


def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    while n > 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    yield n

    # Recursive Solution
def hailstone(n):
    yield n
    if n != 1:
        if n % 2 == 0:
            yield from hailstone(n//2)
        else:
            yield from hailstone(n*3+1)


