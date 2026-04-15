# Iterators wrap up:
class myrange:
    def __init__(self, n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n:
            current = self.i
            self.i += 1
            return current
        else:
            raise StopIteration()

class CountIterator:
    """Wraps an iterator and tracks how many times next() has been called successfully."""

    def __init__(self, iterator):
        self._it = iter(iterator)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        val = next(self._it)
        self._count += 1
        return val

    def num_calls(self):
        """Return the number of items yielded so far."""
        return self._count

ci = CountIterator(range(5))
# >>> for val in ci:
# ...     print(f"val={val}, calls={ci.num_calls()}")
# val=0, calls=1
# val=1, calls=2
# val=2, calls=3
# val=3, calls=4
# val=4, calls=5
# >>> ci.num_calls()
# 5
# >>> next(ci)
# StopIteration
# >>> ci.num_calls()
# 5


from functools import reduce
from operator import add

# A Functional Oriented approach
def acronym_f(words):
    return reduce(add,
                map(lambda w: w[0],
                filter(lambda w: len(w) > 3,
                        words.split(' '))))

# A traditional imperative approach
def acronym_i(words):
    result = ''
    words = words.split(' ')
    for word in words:
        if len(word) > 3:
            result += word[0]
    return result

# A "hybird" approach. Mixes paradigms
def acronym_h(words):
    words = words.split(' ')
    long = filter(lambda w: len(w) > 3, words)
    letters = mapa(lambda w: w[0], long)
    return ''.join(letters)

# Kind of data centric / arrays.
def acronym_list(words):
    return ''.join([w[0] for w in words.split(' ') if len(w) > 3])
