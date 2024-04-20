"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""
# @timeit
def sequential_search(array, element):
    start = max(0, len(array)-1) if array else -1

    for index in range(start+1, -1,-1):
        if array[index] == element:
            return (True, index)

    return False, -1
