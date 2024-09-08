def sum_even_and_even_index(lst):
    return sum(el for i, el in enumerate(lst) if i % 2 == 0 and el % 2 == 0)

print(sum_even_and_even_index([5, 6, 12, 1, 18, 8])) # 30

Explanation:
The function sum_even_and_even_index takes a list as an argument. It uses the enumerate function to iterate over the elements of the list along with their indices. The condition i % 2 == 0 checks if the index is even, and the condition el % 2 == 0 checks if the element is even. If both conditions are satisfied, the element is added to the sum.

Note:
This solution assumes that the list starts at index 0 (which is even), and that by "even positions" you mean the position in the list (or the index in the list), not the value at that position. If by "even positions" you mean the values at the even positions, then the function needs to be slightly modified.
"""

# Test cases
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6]) == 12
assert sum_even_and_even_index([2, 2, 2, 2, 2, 2]) == 12
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1]) == 0
assert sum_even_and_even_index([2]) == 2
assert sum_even_and_even_index([]) == 0
"""
"""
"""
