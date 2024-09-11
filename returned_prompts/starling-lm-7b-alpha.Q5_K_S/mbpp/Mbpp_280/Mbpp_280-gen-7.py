"""
def sequential_search(arr, element):
    boolean = False
    index = -1
    for i in range(len(arr)):
        if arr[i] == element:
            boolean = True
            index = i
    return (boolean, index)

assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""

def sequential_search(arr, element):
    boolean = False
    index = -1
    for i in range(len(arr)):
        if arr[i] == element:
            boolean = True
            index = i
    return (boolean, index)

assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)



