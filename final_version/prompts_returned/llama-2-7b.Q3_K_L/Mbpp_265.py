"""
Write a function that takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""
from typing import List, Any
def list_split(list_, n:int) -> Any:
    """Write a function that takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.
  assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]"""
    result = [[] for _ in range(len(list_))]
    for i, val in enumerate(list_, start=1):
        if not isinstance(val, int) and isinstance(val, float):
            continue
        else:
            if i % n == 0:
                result[-1].append(val)
                del result[-1] #empty list
    return result

print (list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3))
\end{code}