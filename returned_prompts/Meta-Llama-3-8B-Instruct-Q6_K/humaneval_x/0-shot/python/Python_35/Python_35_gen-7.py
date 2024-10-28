def max_element(l: list):
    if not l:
        return None
    return max(l)
    # or return max(iter(l)) for Python 3.7 and below


Explanation:
This function takes a list as an argument and returns the maximum element in the list. The function uses the built-in Python function `max()` which returns the largest item in an iterable or the largest of two or more arguments.

If the list is empty, the function returns `None` to indicate that there is no maximum element. This is a common convention in Python to indicate the absence of a value.

The function can be tested with the provided unit tests. For example, `max_element([1, 2, 3])` should return `3`, and `max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])` should return `123`.