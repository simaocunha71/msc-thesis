
    return " ".join(str(i) for i in range(n+1))


print(string_sequence(0))
print(string_sequence(5))


This function utilizes Python's built-in `range` function and `join` method to concatenate a list of strings into a single string with space-delimited numbers.

It starts from 0 (inclusive) up to n (inclusive), using the `range` function which creates a sequence of numbers starting from 0 up to n (not inclusive). The `str` function is used to convert each number to a string, and the `join` method is used to concatenate the strings into a single string with space-delimited numbers.

The time complexity of this function is O(n), as it needs to iterate over all numbers from 0 to n. The space complexity is also O(n), as it creates a new list of strings of size n.
"""

# -------------------------
"""
