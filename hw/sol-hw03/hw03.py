from operator import add, mul

def square(x):
    return x * x

def identity(x):
    return x

def triple(x):
    return 3 * x

def increment(x):
    return x + 1


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term: a function that takes an index as input and produces a term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    prod, k = 1, 1
    while k <= n:
        prod, k = term(k) * prod, k + 1
    return prod


def funception(func1, begin):
    """ Takes in a function (func1) and a begin value.
    Returns a function (func2) that will find the product of
    func1 applied to the range of numbers from
    begin (inclusive) to end (exclusive)

    >>> def increment(num):
    ...     return num + 1
    >>> def double(num):
    ...     return num * 2
    >>> g1 = funception(increment, 0)
    >>> g1(3)    # increment(0) * increment(1) * increment(2) = 1 * 2 * 3 = 6
    6
    >>> g1(0)    # Returns 1 because begin >= end
    1
    >>> g1(-1)   # Returns 1 because begin >= end
    1
    >>> g2 = funception(double, 1)
    >>> g2(3)    # double(1) * double(2) = 2 * 4 = 8
    8
    >>> g2(4)    # double(1) * double(2) * double(3) = 2 * 4 * 6 = 48
    48
    >>> g3 = funception(increment, -3)
    >>> g3(-1)   # increment(-3) * increment(-2) = -2 * -1 = 2
    2
    """
    def func2(end):
        i = begin
        product = 1
        while i < end:
            product *= func1(i)
            i += 1
        return product
    return func2


def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    def repeater(x):
        k = 0
        while k < n:
            x, k = f(x), k + 1
        return x
    return repeater

