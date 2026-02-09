def greet(name):
    return 'Hello, ' + name + '!'

say_hello = greet

say_hello('CS88')

# Generalizing patterns using arguments

from math import pi, sqrt
from operator import mul, add
from functools import reduce

# Functions as arguments

def square(n):
    return n * n

def sum_numbers(n):
    """Sum the first N natural numbers.
    >>> sum_numbers(5)
    15
    >>> sum_numbers(10)
    55
    """
    total = 0
    for i in range(n + 1):
        total += i
    return total

def sum_squared(n):
    """Sum the first N squares of natural numbers.

    >>> sum_squared(5)
    55
    """
    total = 0
    for i in range(n + 1):
        total += square(i) # i ** 2
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.
    >>> sum_cubes(5)
    225
    """
    total = 0
    for i in range(n + 1):
        total += pow(i, 3)
    return total

def sum_generic(n, func):
    total = 0
    for i in range(n + 1):
        total += func(i)
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.
    >>> summation(5, cube)
    225
    >>> summation(5, identity)
    15
    >>> summation(10, identity)
    55
    """
    total = 0
    print(term)
    for i in range(n + 1):
        total = total + term(i)
    return total

def sum_error(n, term):
    """Sum the first N terms of a sequence.
    """
    total = 0
    for i in range(n + 1):
        total = total + term
    return total


from operator import mul

def pi_term(k):
    # This is the expansion of the terms on the summation slide.
    return 8 / (16*k*k + 12*k + 4*k + 3)

summation(10000, pi_term)

def pi_error(approx):
    return str((1 - summation(approx, pi_term) / pi) * 100) + '%'

def add_one(n):
    return n + 1

def square(n):
    return n * n

# help(map)

def is_even(n):
    return n % 2 == 0

def is_uppercase(word):
    return word[0].capitalize() == word[0]

def shout(word):
    return word.upper()

def embiggen(item):
    "This uses some Python features we don't really cover, but can be fun."
    if type(a) == str:
        return shout(item)
    elif item.isdigit():
        return int(item) * 2
    else:
        return item

cal = 'The University of California at Berkeley'
copycats = 'The University of California Los Angeles'
jc = 'Leland Stanford Junior University'

words = cal.split()
# words
# # ['The', 'University', 'of', 'Califonria', 'at', 'Berkeley']
numbers = range(10)
# [ n * n for n in numbers ]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

square(5)
map(square, numbers)

def emojify(letter):
    """Turn a letter a-z into an emoji.
    """
    return chr(ord(letter) - ord('a') + ord('😀'))

def un_emojify(emoji):
    """Turn an emoji into a letter a-z.
    """
    return chr(ord(emoji) - ord('😀') + ord('a'))


# <map object at 0x100fe5940>
# range(10)
# range(0, 10)
list(map(square, numbers))
def first_letter(word):
    return word[0]

def long_word(word):
    return len(word) > 3

first_letter('Berkeley')
list(map(first_letter, words))

words
# ['The', 'University', 'of', 'Califonria', 'at', 'Berkeley']
def is_even(n):
    return n % 2 == 0
# ...
is_even(3)
# False
# range(0, 10)
[ n for n in numbers if is_even(n) ]
filter(is_even, numbers)
# <filter object at 0x101069b50>
list(filter(is_even, numbers))

def long_word(word):
    return len(word) > 3

long_word('of')
# False
list(filter(long_word, words))
# ['University', 'Califonria', 'Berkeley']
# >>>
# >>>
reduce
# <built-in function reduce>
add(1, 2)
# 3
reduce(add, numbers)
# 45
list(numbers)


def keep_words(word):
    specials = ['Los']
    return word in specials or long_word(word)

def acronym(text):
    words = text.split()
    return reduce(add, map(first_letter, filter(long_word, words)))


def acronym_hof(sentence, filter_fn):
    """
    >>> acronym_hof(cal, keep_words)
    "UCB"
    >>> acronym_hof(copycats, keep_words)
    "UCLA"
    >>> acronym_hof(jc, keep_words)
    "LSJU"
    """
    words = sentence.split()
    return reduce(add, map(first_letter, filter(filter_fn, words)))

def group_by(result_or_start, next_item):
    """
    Combine two item pairs by their first key.
    >>> courses = ['DATA C88C', 'DATA 8', 'POLSCI 2', 'MATH 54']
    >>> depts = [ course.split() for course in courses ]
    >>> reduce(group_by, depts)
    [['DATA', ['C88C', '8']], ['POLSCI', ['2']], ['MATH', ['54']]]
    """
    item = next_item
    if not result_or_start or type(result_or_start[0]) != list:
        result = [ [result_or_start[0], [ result_or_start[1] ] ] ]
    else:
        result = result_or_start
    keys = [ pair[0] for pair in result ]
    if item[0] in keys:
        index = keys.index(item[0])
        pair = result[index]
        pair[1].append(item[1])
    else:
        result.append([ item[0], [ item[1] ] ])
    return result

def group_by_count(result_or_start, next_item):
    """
    Aggregate counts two item pairs by their first key.
    >>> courses = ['DATA C88C', 'DATA 8', 'POLSCI 2', 'MATH 54']
    >>> depts = [ course.split() for course in courses ]
    >>> reduce(group_by_count, depts)
    [['DATA', 2], ['POLSCI', 1], ['MATH', 1]]
    """
    item = next_item
    if not result_or_start or type(result_or_start[0]) != list:
        result = [ [ result_or_start[0], 1 ] ]
    else:
        result = result_or_start
    keys = [ pair[0] for pair in result ]
    if item[0] in keys:
        index = keys.index(item[0])
        pair = result[index]
        pair[1] = pair[1] + 1
    else:
        result.append([ item[0], 1 ])
    return result



def add_one(n):
    return n + 1

add_one(3)

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_1 = make_adder(1)
x = add_1(3)

add_4 = make_adder(4)
add_4(5)

def compose(f, g):
    def h(x):
      return f(g(x))
    return h

add_2 = make_adder(2)
add_3 = make_adder(3)
x = add_2(x)

add_5 = compose(add_2, add_3)
y = add_5(x)

# compose an add_2 function with square
# square(add_2(3))
z = compose(square, make_adder(2))(3)

def leq_maker(c):
    def leq(val):
        return val <= c
    return leq

leq_maker(5)
leq_maker(5)(3)
