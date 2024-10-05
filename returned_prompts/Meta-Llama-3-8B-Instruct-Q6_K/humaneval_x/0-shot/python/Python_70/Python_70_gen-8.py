    # Sort the list first
    lst.sort()
    result = []
    while lst:
        # Add the smallest number
        result.append(lst.pop(0))
        # If the list is not empty, add the largest number
        if lst:
            result.append(lst.pop())
    return result

# Test cases
print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []

# Test with negative numbers
print(strange_sort_list([-5, -2, 1, 4]))  # [-5, 4, -2, 1]
print(strange_sort_list([-2, -1, 0, 1]))  # [-2, 1, -1, 0]

# Test with duplicates
print(strange_sort_list([1, 2, 2, 3]))  # [1, 3, 2, 2]
print(strange_sort_list([2, 2, 2, 2]))  # [2, 2, 2, 2]







