"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""
from typing import List

def find_dissimilar(a: List[int], b: List[int]) -> List[int]:
    hash_a = {}
    for i in a:
        if i not in hash_a.keys():
            hash_a[i] = 1
        else:
            hash_hash_a[i] += 1
    
    hash_b = {}
    for i in b:
        if i not in hash_b.keys():
            hash_b[i] = 1
        else:
            hash_hash_b[i] += 1
    
    dissimilar_elements = []
    if hash_a != hash_b:
        for i, element in enumerate(a):
            if (hash_a[element] + hash_hash_a[element]) == hash_b[element]:
                continue
            else:
                dissimilar_elements.append(i)
    return dissimilar_elements