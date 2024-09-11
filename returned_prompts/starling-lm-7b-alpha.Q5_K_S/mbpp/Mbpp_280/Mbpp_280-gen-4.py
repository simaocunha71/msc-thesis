"""
def sequential_search(array, element):
    if element in array:
        for i in range(len(array)):
            if array[i] == element:
                return True, i
    else:
        return False, -1

sequential_search([11,23,58,31,56,77,43,12,65,19],31)
"""

