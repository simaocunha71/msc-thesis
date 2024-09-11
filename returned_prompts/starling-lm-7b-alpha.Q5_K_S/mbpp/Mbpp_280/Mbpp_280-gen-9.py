"""
def sequential_search(arr, element):
    for index, value in enumerate(arr):
        if value == element:
            return (True, index)
    return (False, -1)

# Test
print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))  # (True, 3)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],10))  # (False, -1)
"""

def sequential_search(arr, element):
    for index, value in enumerate(arr):
        if value == element:
            return (True, index)
    return (False, -1)

# Test
print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))  # (True, 3)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],10))  # (False, -1)








"""
