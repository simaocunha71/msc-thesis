"""
def interleave_lists(list_a, list_b, list_c):
    return [x for i, x in enumerate(list_a) for y in list_b] + [x for i, x in enumerate(list_b) for y in list_c] + [x for i, x in enumerate(list_c) for y in list_a]

def interleave_lists(list_a, list_b, list_c):
    return (list(zip(list_a, list_b, list_c)))

def interleave_lists(list_a, list_b, list_c):
    return list(itertools.zip_longest(list_a, list_b, list_c))

def interleave_lists(list_a, list_b, list_c):
    return list(chain.from_iterable(zip(list_a, list_b, list_c)))

def interleave_lists(list_a, list_b, list_c):
    return list(itertools.chain(zip(list_a, list_b, list_c)))
"""

# Using itertools.chain
from itertools import chain

def interleave_lists(list_a, list_b, list_c):
    return list(chain.from_iterable(zip(list_a, list_b, list_c)))

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))  # [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]

# Using itertools.zip_longest
from itertools import zip_longest

def interleave_lists