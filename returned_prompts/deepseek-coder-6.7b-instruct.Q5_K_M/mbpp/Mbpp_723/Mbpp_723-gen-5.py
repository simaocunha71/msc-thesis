def count_same_pair(lst1, lst2):
    assert len(lst1) == len(lst2)
    return sum(1 for a, b in zip(lst1, lst2) if a == b)

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])) # Returns: 4

Explanation:
The function counts the number of elements where the two lists have the same value. It does this by iterating through the two lists simultaneously (using the zip function), and checking if the elements at each index are equal. If they are, the counter is incremented by 1. The sum function then returns the total count.
"""
