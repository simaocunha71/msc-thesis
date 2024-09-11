"""
def sequential_search(arr, elem):
    result = False
    pos = -1
    for i in range(len(arr)):
        if arr[i] == elem:
            result = True
            pos = i
            break
    return (result, pos)
"""

def sequential_search(arr, elem):
    result = False
    pos = -1
    for i in range(len(arr)):
        if arr[i] == elem:
            result = True
            pos = i
            break
    return (result, pos)

# assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
# assert sequential_search([11,23,58,31,56,77,43,12,65,19],58) == (True, 2)
# assert sequential_search([11,23,58,31,56,77,43,12,65,19],5) == (False,-1)
# assert sequential_search([11,23,58,31,56,77,43,12,65,19],66) == (False,-1)

def sequential_search2(arr, elem):
    result = False
    pos = -1
    for i in range(len(arr)):
        if arr[i] == elem:
            result = True
            pos = i
            break
    return (result, pos)

# assert sequential_search2([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
# assert sequential_search2([11,23,58,31,56,77,43,12,65,19],58) == (True, 2)
# assert sequential_search2([11,23,58,31,56,7