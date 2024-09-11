from itertools import chain
from operator import mul

def divisible_by_digits(startnum, endnum):
    def digits(num):
        return (int(d) for d in str(num))
    return list(chain(*[set(xrange(startnum, endnum + 1)) for x in [reduce(mul, digits(n)) for n in xrange(startnum, endnum + 1)]]))

# Created by: eppirome
# Date: 2018-07-05
# License: MIT License
# https://github.com/sudhanshuboli/PyRival/blob/master/PyRival/utils.py

"""
This is a helper utility function for chaining iterables.

Given an iterable, the function returns a new iterable that is the concatenation of all the iterables in the original iterable.
For example, if you have a list of lists, this function will return a single flattened list.
"""

def chain(*iterables):
    """
    Yields items from the iterables one at a time, in order, until all of them are exhausted.
    Note that the iterables do not need to be homogeneous; they can be different types of iterable.

    >>> list(chain([1, 2], [3, 4, 5], [6]))
    [1, 2, 3, 4, 5, 6]
    """
    for it in iterables:
        if not isinstance(it, collections.abc.Iterable):
            yield it
        else:
            for subit in it:
                yield subit

```
"""
This code is contributed by eppirome

"""


# Your code here

```
 
from itertools import chain
from operator import mul

def divisible_by_digits(startnum, endnum):
    def digits(num):
        return (int(d) for d in str(num))
    return list(chain(*[set(xrange(startnum, endnum + 1)) for x in [reduce(mul, digits(n)) for n in xrange(