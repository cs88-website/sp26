def partition(n):
    """Return the number of partitions of positive integer n.

    >>> partition(5)
    7
    >>> partition(10)
    42
    >>> partition(15)
    176
    >>> partition(20)
    627
    """
    "*** YOUR CODE HERE ***"


def merge_numbers(n1, n2):
    """Merges two numbers that have decreasing digits.

    >>> merge_numbers(31, 42)
    4321
    >>> merge_numbers(21, 0)
    21
    >>> merge_numbers(21, 31)
    3211
    """
    "*** YOUR CODE HERE ***"



def insert_into_all(item, lsts):
    """Assuming that lsts is a list of lists, return a new list consisting of
    all the lists in lsts, but with item added to the front of each.

    >>> lsts = [[], [1, 2], [3]]
    >>> insert_into_all(0, lsts)
    [[0], [0, 1, 2], [0, 3]]
    """
    return [[item] + lst for lst in lsts]

def non_decrease_subseqs(s):
    """Return a nested list of all subsequences of S (a list of lists) 
    for which the elements of the subsequence are nondecreasing. The 
    subsequences can appear in any order. You can assume S is a list.

    >>> seqs = non_decrease_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> non_decrease_subseqs([])
    [[]]
    >>> seqs2 = non_decrease_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    def subseq_helper(s, prev):
        if not s:
            return ____________________
        elif s[0] < prev:
            return ____________________
        else:
            a = ______________________
            b = ______________________
            return insert_into_all(________, ______________) + ________________
    return subseq_helper(____, ____)

