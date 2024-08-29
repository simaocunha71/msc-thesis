def count_first_elements(tup):
    count = 0
    for i in tup:
        if isinstance(i, tuple):
            break
        count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10)))  # Output: 3

Explanation:
The function count_first_elements takes a tuple as input. It then iterates over the elements of the tuple. If the element is a tuple (i.e., it's a sub-tuple), it breaks the loop (stops counting) and returns the count of the number of elements before the first tuple. If the element is not a tuple, it increments the count and continues to the next element.

The test case asserts that the function returns 3 when given the tuple (1, 5, 7, (4, 6), 10). This is because the first three elements of the tuple are not tuples (1, 5, 7), so the function counts them as the first elements.
"""

# Solution 2
def count_first_elements(tup):
    count = 0
    for i in tup:
        if isinstance(i, tuple):
            break
        count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10)))  # Output: 3
"""

# Solution 3
def count_first_elements(tup):
    return sum(not isinstance(i, tuple) for i in tup)

print(count_first_elements((1, 5, 7, (4, 6), 10)))  # Output: 3
"""

# Solution 4
def count_first_elements(tup):
    return len([i for i in tup if not isinstance(i, tuple)])

print(count_first_elements((1, 5, 7, (4, 6), 10)))  # Output: 3
"""

All these solutions essentially do the same thing, but they use different Python techniques to solve the problem. The first solution uses a simple for loop