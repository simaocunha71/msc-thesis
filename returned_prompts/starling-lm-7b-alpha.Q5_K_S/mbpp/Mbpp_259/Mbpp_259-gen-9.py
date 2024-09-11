from itertools import chain, starmap, zip_longest
from operator import itemgetter
from functools import reduce


def maximize_elements(t1, t2):
    return list(reduce(lambda x, y: starmap(max, zip_longest(x, y, fillvalue=itemgetter(0))),
                       zip(t1, t2)))


# Python3 program to print maximum elements in two tuples
# in a single tuple
"""
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)),
                         ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""

# This code is contributed by Anant Agarwal.

# Python3 program to print maximum elements in two tuples
# in a single tuple
def maximize_elements(t1, t2):
    return list(reduce(lambda x, y: starmap(max, zip_longest(x, y, fillvalue=itemgetter(0))),
                       zip(t1, t2)))


# Python3 program to print maximum elements in two tuples
# in a single tuple
def maximize_elements(t1, t2):
    return list(reduce(lambda x, y: starmap(max, zip_longest(x, y, fillvalue=itemgetter(0))),
                       zip(t1, t2)))


# This code is contributed by Anant Agarwal.
# Python3 program to print maximum elements in two tuples
# in a single tuple
def maximize_elements(t1, t2):
    return list(reduce(lambda x, y: starmap(max, zip_longest(x, y, fillvalue=itemgetter(0))),
                       zip(t1, t2)))


# This code is contributed by Anant Agarwal.

```
  
  
# Python3 program to print maximum elements in two tuples
# in a