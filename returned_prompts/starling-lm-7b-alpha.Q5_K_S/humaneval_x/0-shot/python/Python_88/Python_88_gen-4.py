# Solution
def sort_array(array):
    sum_first_last = array[0] + array[-1]
    if sum_first_last % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

# Test cases
print(sort_array([]))  # []
print(sort_array([5]))  # [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # [6, 5, 4, 3, 2, 1, 0]


# Solution 2
def sort_array(array):
    return sorted(array, key=lambda x: array[0] + array[-1] % 2)

# Test cases
print(sort_array([]))  # []
print(sort_array([5]))  # [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # [6, 5, 4, 3, 2, 1, 0]


# Solution 3
def sort_array(array):
    return sorted(array, key=lambda x: x[0] + x[-1] % 2)

# Test cases
print(sort_array([]))  # []
print(sort_array([5]))  # [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # [6, 5, 4, 3, 2, 1