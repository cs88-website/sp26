class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        "*** YOUR CODE HERE ***"


def amplify(f, x):
    """Yield the values x, f(x), f(f(x)), ... that are all truthy values
    and stop yielding once the sequence reaches the first falsy value.

    >>> gen1 = amplify(lambda s: s[1:], 'boxes')
    >>> [next(gen1) for _ in range(5)]
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> try:
    ...     next(gen1)
    ... except StopIteration:
    ...     print('Correctly raised StopIteration')
    ... else:
    ...     print('Expected StopIteration error but was not raised')
    Correctly raised StopIteration
    >>> gen2 = amplify(lambda x: x // 2 - 1, 14)
    >>> [next(gen2) for _ in range(3)]
    [14, 6, 2]
    >>> try:
    ...     next(gen2)
    ... except StopIteration:
    ...     print('Correctly raised StopIteration')
    ... else:
    ...     print('Expected StopIteration error but was not raised')
    Correctly raised StopIteration
    """
    "*** YOUR CODE HERE ***"


def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    def __init__(self, cur):
        self.cur = cur

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        """So that we can use this iterator as an iterable."""
        return self

