def sub_list(l1, l2):
    """
    :type l1: List[int]
    :type l2: List[int]
    :rtype: List[int]
    """
    return [a - b for a, b in zip(l1, l2)]

# 1
# 2
# 3
# 4
# 5
# 6
# -3
# -3
# -3


"""
Write a function to add two lists element-wise.
assert add_list([1, 2, 3],[4,5,6])==[5,7,9]
"""
def add_list(l1, l2):
    """
    :type l1: List[int]
    :type l2: List[int]
    :rtype: List[int]
    """
    return [a + b for a, b in zip(l1, l2)]

# 1
# 2
# 3
# 4
# 5
# 6
# 5
# 7
# 9

"""
Write a function to multiply two lists element-wise.
assert mul_list([1, 2, 3],[4,5,6])==[4,10,18]
"""
def mul_list(l1, l2):
    """
    :type l1: List[int]
    :type l2: List[int]
    :rtype: List[int]
    """
    return [a * b for a, b in zip(l1, l2)]

# 1
# 2
# 3
# 4
# 5
# 6
# 4
# 10
# 18

```

```
"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""

def sub_list(l1, l2):
    """
    :type l1: List[int]
    :type l2: List[int]
   