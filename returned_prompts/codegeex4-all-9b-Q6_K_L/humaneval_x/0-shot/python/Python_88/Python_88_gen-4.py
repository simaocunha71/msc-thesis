def sort_array(array):
    if len(array) < 2: return array
    first, last = array[0], array[-1]
    if (first + last) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

print(sort_array([2, 4, 3, 0, 1, 5]))
print(sort_array([2, 4, 3, 0, 1, 5, 6]))