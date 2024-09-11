"""
Here is the function to find whether all the given tuples have equal length or not:

"""

from collections import Counter

def get_equal(tup):
    return len(Counter(map(len, tup))) == 1




# Code taken from GeeksforGeeks. I have made some modifications to it
# Original source: https://www.geeksforgeeks.org/python-program-to-find-whether-all-the-given-tuples-have-equal-length-or-not/
"""

"""

To check if all the given tuples have equal length or not, you can follow these steps:

1. Use the `map` function to get a list of the lengths of all the tuples.
2. Use the `Counter` function from the `collections` module to count the occurrence of each length in the list.
3. Check if the length of the Counter object is equal to 1. If it is, then all the tuples have the same length; otherwise, they don't.

The function `get_equal` takes a list of tuples as input and returns `True` if all the tuples have the same length, and `False` otherwise. It uses the `Counter` function to count the occurrence of each length in the list of tuple lengths, and then checks if the length of the Counter object is equal to 1. If it is, then all the tuples have the same length; otherwise, they don't.

You can test the function by calling it with a list of tuples as an argument, like this: `get_equal([(11, 22, 33), (44, 55, 66)])`. This will return `True` because both tuples have the same length (3).

I hope this helps! Let me know if you have any more questions.

-WB"""

"""

Here's an example of how you can use the `get_equal` function:

```python
tup1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
tup2 = [(10, 11, 