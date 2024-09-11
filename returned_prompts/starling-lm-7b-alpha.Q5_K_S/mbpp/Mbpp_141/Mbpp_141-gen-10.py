"""
def pancake_sort(array):
    while array != sorted(array):
        max_value = max(array)
        max_index = array.index(max_value)
        array.insert(0, array.pop(max_index + 1))
    return array
"""

def pancake_sort(array):
    while array != sorted(array):
        max_value = max(array)
        max_index = array.index(max_value)
        array.insert(0, array.pop(max_index))
    return array



# assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
# print(pancake_sort([15, 79, 25, 38, 69]))
# print(pancake_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
# print(pancake_sort([3, 4, 5, 6, 7, 8, 9]))

"""
    def pancake_sort(array):
        while array != sorted(array):
            max_value = max(array)
            max_index = array.index(max_value)
            array.insert(0, array.pop(max_index + 1))
        return array
"""

"""
    def pancake_sort(array):
        while array != sorted(array):
            max_value = max(array)
            max_index = array.index(max_value)
            array.insert(0, array.pop(max_index))
        return array
"""

"""
    def pancake_sort(array):
        while array != sorted(array):
            max_value = max(array)
            max_index = array.index(max_value)
            array.insert(0, array.pop(max_index + 1))
        return array
"""


"""
    def pancake_sort(array):
        while array