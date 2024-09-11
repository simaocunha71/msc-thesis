def sum_list(list1, list2):
    """
    Returns the sum of each pair of elements in two lists.

    >>> sum_list([10,20,30],[15,25,35])
    [25,45,65]
    """
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result


# Test the function
assert sum_list([10,20,30],[15,25,35])==[25,45,65]

def sum_list_v2(list1, list2):
    """
    Returns the sum of each pair of elements in two lists, using list comprehension.

    >>> sum_list_v2([10,20,30],[15,25,35])
    [25,45,65]
    """
    return [list1[i] + list2[i] for i in range(len(list1))]


# Test the function
assert sum_list_v2([10,20,30],[15,25,35])==[25,45,65]

def sum_list_v3(list1, list2):
    """
    Returns the sum of each pair of elements in two lists, using the built-in zip function.

    >>> sum_list_v3([10,20,30],[15,25,35])
    [25,45,65]
    """
    return [a+b for a, b in zip(list1, list2)]


# Test the function
assert sum_list_v3([10,20,30],[15,25,35])==[25,45,65]

def sum_list_v4(list1, list2):
    """
    Returns the sum of each pair of elements in two lists, using the built-in itertools.zip_longest function.

    >>> sum_list