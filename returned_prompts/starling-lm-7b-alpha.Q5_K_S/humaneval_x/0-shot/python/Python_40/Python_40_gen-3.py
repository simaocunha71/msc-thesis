

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    from itertools import combinations
    l = sorted(l)
    for comb in combinations(l, 3):
        if sum(comb) == 0 and len(set(comb)) == 3:
            return True
    return False

# Created by: Madhav Khakhar
# Date Created: Oct 24, 2020
# Last Modified: Oct 24, 2020

# Code Reviewers: Ray Wang

# This program checks whether a list of integers has a
# triplet of distinct elements that sum to zero.
```
     		 			 	 	 	 					 	 		
```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_