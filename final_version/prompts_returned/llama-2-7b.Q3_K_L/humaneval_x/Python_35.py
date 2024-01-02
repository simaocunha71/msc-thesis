

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return None
    else:
        # we can stop the loop after finding max element. So, we don't need while condition to iterate through list for all elements.
        for i in range(len(l)):
            if l[i] > max_element():
                return max_element()
            else:
                pass
    print("No such element")
    return None
