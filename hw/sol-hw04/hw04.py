def smooth(f, dx):
    """Returns the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> round(smooth(square, 1)(0), 3)
    0.667
    """
    return lambda x: (f(x - dx) + f(x) + f(x + dx)) / 3

def n_fold_smooth(f, dx, n):
    """Returns the n-fold smoothed version of f

    >>> square = lambda x: x ** 2
    >>> round(n_fold_smooth(square, 1, 3)(0), 3)
    2.0
    """
    return repeated(lambda g: smooth(g, dx), n)(f)

def repeated(f, n):
    """Returns a single-argument function that takes a value, x, and applies
    the single-argument function F to x N times.
    >>> repeated(lambda x: x*x, 3)(2)
    256
    """
    def h(x):
        for k in range(n):
            x = f(x)
        return x
    return h


def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b)  # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a  # a's prefix [1,1,3,2] is replaced with b's prefix [4,3]
    [4, 3, 1, 1, 4]
    >>> b  # b's prefix [4,3] is replaced with a's prefix [1,1,3,2]
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)  # No prefixes with equal sum
    'No deal!'
    >>> b  # b remains unchanged
    [1, 1, 3, 2, 2, 7]
    >>> c  # c remains unchanged
    [3, 3, 2, 4, 1]
    >>> trade(a, c)  # Trades 4+3+1=8 for 3+3+2=8
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    >>> d = [1, 1]
    >>> e = [2]
    >>> trade(d, e)  # Trades 1+1=2 for 2=2
    'Deal!'
    >>> d
    [2]
    >>> e
    [1, 1]
    """
    m, n = 1, 1

    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])
    while m <= len(first) and n <= len(second) and not equal_prefix():
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1

    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'


def filter(condition, lst):
    """Filters lst with condition using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    for e in lst[:]:
        if not condition(e):
            lst.remove(e)

# Alternate solution
def filter2(condition, lst):
    elems_to_remove = [e for e in lst if not condition(e)]
    for e in elems_to_remove:
        lst.remove(e)

