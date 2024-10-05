def filter_integers(values: List[Any]) -> List[int]:
    return [i for i in values if isinstance(i, int)]


# Other solutions
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [i for i in values if type(i) == int]

def filter_integers(values: List[Any]) -> List[int]:
    return [i for i in values if isinstance(i, int)]

def filter_integers(values: List[Any]) -> List[int]:
    return [i for i in values if type(i) is int]


# More readable version
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers


# Using itertools.filterfalse
from typing import List, Any
import itertools

def filter_integers(values: List[Any]) -> List[int]:
    return list(itertools.filterfalse(lambda x: not isinstance(x, int), values))

# Using functools.reduce
from typing import List, Any
import functools

def filter_integers(values: List[Any]) -> List[int]:
    return functools.reduce(list.__add__, map(lambda x: x if isinstance(x, int) else [], values))

# Using list comprehension with itertools.ifilterfalse
from typing import List, Any
import itertools

def filter_integers(values: List[Any]) -> List[int]:
    return list(itertools.ifilterfalse(lambda x: not isinstance(x, int), values))

# Using list comprehension with itertools.ifilter
from typing import List, Any
import itertools

def filter_integers(values: List[Any]) -> List[int]:
    return list(itertools.ifilter(lambda x: isinstance(x, int), values))


# Using list comprehension with functools.reduce
from typing import List