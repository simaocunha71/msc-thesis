"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""
from typing import Union
def minimum(a:Union[int], b):
    if a < b: return a
    else return b
\end{code}