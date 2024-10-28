def pancake_sort(array):
    while array != sorted(array):
        max_value = max(array)
        max_index = array.index(max_value)
        array.insert(0, array.pop(max_index))
    return array