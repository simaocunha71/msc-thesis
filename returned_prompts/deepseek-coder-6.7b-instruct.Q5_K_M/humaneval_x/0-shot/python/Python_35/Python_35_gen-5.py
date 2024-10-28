

def max_element(l: list):
    return max(l)
"""


def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)


# Test cases
print(max_element([1, 2, 3]))  # 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # 123
<jupyter_output>
3
123
<jupyter_text>
Question 2Given a list of integers, write a function to return the sum of all the positive numbers in the list.
<jupyter_code>
"""
