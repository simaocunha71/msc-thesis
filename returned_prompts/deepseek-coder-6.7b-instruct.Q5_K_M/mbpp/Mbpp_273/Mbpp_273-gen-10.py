def substract_elements(tuple1, tuple2):
    return tuple(i - j for i, j in zip(tuple1, tuple2))

print(substract_elements((10, 4, 5), (2, 5, 18)))

"""
Output:
(8, -1, -13)
"""

Explanation:
The function uses the built-in zip function to iterate over the two tuples at the same time, and subtracts the corresponding elements from tuple1 from tuple2.
The zip function returns an iterator of tuples, where the first element in each passed iterator is paired together, and then the second element in each passed iterator are paired together etc.
If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
"""

# 2. Create a function that takes a list of integers and returns a new list with the squares of the integers.

