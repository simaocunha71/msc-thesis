"""
def combinations_list(lst):
    result = []
    for i in range(len(lst) + 1):
        for subset in itertools.combinations(lst, i):
            result.append(list(subset))
    return result

print(combinations_list(['orange',  'red', 'green', 'blue']))
"""

B:
"""
def combinations_list(lst):
    return [list(subset) for i in range(len(lst) + 1) for subset in itertools.combinations(lst, i)]

print(combinations_list(['orange',  'red', 'green', 'blue']))
"""

C:
"""
import itertools

def combinations_list(lst):
    return list(itertools.chain.from_iterable(itertools.combinations(lst, r) for r in range(len(lst)+1)))

print(combinations_list(['orange',  'red', 'green', 'blue']))
"""

D:
"""
from itertools import chain, combinations

def combinations_list(lst):
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))

print(combinations_list(['orange',  'red', 'green', 'blue']))
"""

E:
"""
from itertools import chain, combinations

def combinations_list(lst):
    return list(chain(*[combinations(lst, r) for r in range(len(lst)+1)]))

print(combinations_list(['orange',  'red', 'green', 'blue']))
"""

F:
"""
def combinations_list(lst):
    return [list(x) for x in chain(*[combinations(lst, r) for r in range(len(lst)+1)])]

print(combinations_list(['orange',  'red', 'green', 'blue']))
"""

G:
"""
def combinations_list(lst):
    return [list(x) for