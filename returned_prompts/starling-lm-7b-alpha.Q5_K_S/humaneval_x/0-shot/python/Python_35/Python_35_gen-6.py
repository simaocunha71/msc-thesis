

def max_element(l: list):
    maximum = l[0]
    for i in range(1, len(l)):
        if l[i] > maximum:
            maximum = l[i]
    return maximum


# Test
print(max_element([1, 2, 3]))  # 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # 123


# Recursive
def max_element_r(l: list):
    """Return maximum element in the list.
    >>> max_element_r([1, 2, 3])
    3
    >>> max_element_r([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if len(l) == 0:
        return None
    elif len(l) == 1:
        return l[0]
    else:
        max_num = max_element_r(l[1:])
        if max_num > l[0]:
            return max_num
        else:
            return l[0]


print(max_element_r([1, 2, 3]))  # 3
print(max_element_r([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # 123

```

The `max_element` function returns the maximum element in the list. It initializes the maximum with the first element of the list and then iterates through the rest of the elements in the list. If a new element is greater than the current maximum, it replaces the maximum. Finally, it returns the maximum.

The `max_element_r` function is a recursive version of the `max_element` function. It first checks if the list is empty and if so, it returns None. If the list contains only one element, it returns that element as the maximum. Otherwise