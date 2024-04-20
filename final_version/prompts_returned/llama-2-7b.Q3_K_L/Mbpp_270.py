"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
from typing import List

def sum_even_and_even_index(lst: List[int]) -> int:
    """return the sum of even numbers at even positions
    """
    return [i for i in lst if i % 2 == 0][::2] + \
           [i for i in lst if i % 2 == 0][1:-1]
\end{code}

Answer: \begin{code}
def sum_even_and_even_index(lst):
    """ Return the sum of even numbers at even positions.
    """
    return (
        [i for i in lst if i % 2 == 0][::2] +
        [i for i in lst if i % 2 == 0][1:-1]
    )
\end{code}