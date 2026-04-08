

def iter_fib(n):
    x, y = 0, 1
    for _ in range(n):
       x, y = y, x+y
    return x


def fib(n): # Recursive
    if n < 2:
       return n
    return fib(n - 1) + fib(n - 2)


fib_results = {}
def memo_fib(n): # Look up values in our dictionary.
    global fib_results
    if n in fib_results:
        print(f'found {n} -> {fib_results[n]}')
        return fib_results[n]
    if n < 2:
        fib_results[n] = n
        return n
    result = memo_fib(n - 1) + memo_fib(n - 2)
    fib_results[n] = result
    return result

from functools import cache

# We use a different name just to make it clear.
@cache
def cache_fib(n): # Recursive
    if n < 2:
        return n
    return cache_fib(n - 1) + cache_fib(n - 2)

# However, we do not need to use the decorator like this:
alt_cache_fib = cache(fib)


##### Lots of examples
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(lst, target):
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def binary_search_rec(lst, target, lo=0, hi=None):
    if hi is None:
        hi = len(lst) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search_rec(lst, target, mid + 1, hi)
    else:
        return binary_search_rec(lst, target, lo, mid - 1)

def fast_pow(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result

def mystery_b(n):
    if n == 0:
        return [[]]
    rest = mystery_b(n - 1)
    return rest + [s + [n] for s in rest]
