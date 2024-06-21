"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
import collections
from typing import List

def similar_elements(seq1: list, seq2: list) -> Set[int]:
    """Return the set of elements that appear in both sequences"""
    # convert to a single list
    seq = [x for sublist in (seq1 + seq2) for x in sublist]
    
    # return the set of common numbers between the two lists.
    return {int(s): s for s in seq}
