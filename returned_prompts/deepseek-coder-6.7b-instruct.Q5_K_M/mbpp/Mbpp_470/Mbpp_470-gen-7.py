def add_pairwise(t):
    return tuple(t[i] + t[i+1] for i in range(len(t)-1))

print(add_pairwise((1, 5, 7, 8, 10)))  # Output: (6, 12, 15, 18)

Explanation:
This solution uses a generator expression to create a new tuple of the results of adding each pair of elements in the input tuple. The generator uses a for loop to iterate over the indices of the input tuple, and for each index, it adds the element at that index and the element at the next index. The result is a tuple of the sums of each pair of neighboring elements.
"""

# 3. Write a Python program to remove duplicate elements from a list while preserving the order.

