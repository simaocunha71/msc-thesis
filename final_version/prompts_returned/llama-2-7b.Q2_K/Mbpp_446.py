"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
from typing import Dict, List

def count_Occurrence (tu , l ):
    count = {}   # type: Dict
    for e in tu:
        if e not in count :
            count[e] = 1
        else:
            count[e] += 1    
    return [  ] + list(map(lambda x,y: (x,count[x]) ,l , l ))

# time and space complexity O(ElogE)
