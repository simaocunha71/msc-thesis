def sort_array(array):
    if not array:
        return []
    elif len(array) == 1:
        return array
    else:
        if (array[0] + array[-1]) % 2 == 0:
            array = sorted(array, reverse=True)
        else:
            array = sorted(array)
        return array

print(sort_array([]))
print(sort_array([5]))
print(sort_array([2, 4, 3, 0, 1, 5]))
print(sort_array([2, 4, 3, 0, 1, 5, 6]))