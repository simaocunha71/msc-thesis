"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""
from typing import List, Tuple

def index_minimum(tuples:List[Tuple]):
    """
    :type tuples: List[Tuple[str, int]]
    :rtype: str
    """
    res = ''
    for t in sorted(tuples, key=lambda x:x[1], reverse=True):
        if res != '': 
            return res
        
        res += f'{t[0]}'
    return res