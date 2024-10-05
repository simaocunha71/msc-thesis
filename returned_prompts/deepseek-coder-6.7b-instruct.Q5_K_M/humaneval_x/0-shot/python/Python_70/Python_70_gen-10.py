
    lst.sort()
    result = []

    while lst:
        result.append(lst.pop(0))  # Take minimum
        if lst:
            result.append(lst.pop())  # Take maximum

    return result


print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []


# Alternative solution

def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) ==  [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) ==  [5, 5, 5, 5]
    strange_sort_list([]) ==  []
    '''
    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))  # Take minimum
        if lst:
            result.append(lst.pop(-1))  # Take maximum
    return result


print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []

# This is a solution using the built-in sorting function and popping the first and last elements of the list to get the minimum and maximum values. The result is a new list with the minimum and maximum values interchanged in each pair.
<jupyter