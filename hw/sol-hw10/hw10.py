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
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

    def __iter__(self):
        self.current = self.start
        return self


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
    while x:
        yield x
        x = f(x)


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
    while n >= 0:
        yield n
        n = n - 1


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
        if self.cur < 0:
            raise StopIteration
        self.cur -= 1
        return self.cur + 1

    def __iter__(self):
        """So that we can use this iterator as an iterable."""
        return self

