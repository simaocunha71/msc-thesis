def count_first_elements(tup):
    count = 0
    for i in tup:
        if isinstance(i, tuple):
            break
        count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10)))  # Outputs: 3

Explanation:
The function iterates over the given tuple. If it encounters an element that is not a tuple, it increases the count. It breaks the loop as soon as it encounters a tuple, as we've counted all the elements that occur before the first tuple.
"""

# 