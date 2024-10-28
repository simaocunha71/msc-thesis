def sort_array(array):
    if not array or len(array) == 1:
        return array
    else:
        if (array[0] + array[-1]) % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)

print(sort_array([])) # => []
print(sort_array([5])) # => [5]
print(sort_array([2, 4, 3, 0, 1, 5])) # => [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6])) # => [6, 5, 4, 3, 2, 1, 0]