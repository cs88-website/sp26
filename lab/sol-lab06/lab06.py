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
    return part_max(n, n)

def part_max(n, m):
    """Return the number of partitions of n using integers up to m.

    >>> part_max(5, 3)
    5
    """
    if n < 0 or m <= 0:
        return 0
    if n == 0:
        return 1
    return part_max(n-m, m) + part_max(n, m-1)


def merge_numbers(n1, n2):
    """Merges two numbers that have decreasing digits.

    >>> merge_numbers(31, 42)
    4321
    >>> merge_numbers(21, 0)
    21
    >>> merge_numbers(21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge_numbers(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge_numbers(n1, n2 // 10) * 10 + n2 % 10



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
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:], prev)
        else:
            a = subseq_helper(s[1:], s[0])
            b = subseq_helper(s[1:], prev)
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, 0)

