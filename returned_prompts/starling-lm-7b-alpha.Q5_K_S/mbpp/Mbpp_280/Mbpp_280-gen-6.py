def sequential_search(array, element):
    result = (False, -1)
    for i in range(len(array)):
        if array[i] == element:
            result = (True, i)
    return result


# Testing
print(sequential_search([11,23,58,31,56,77,43,12,65,19],31)) # (True, 3)
print(sequential_search([1,2,3,4,5], 7)) # (False, -1)
print(sequential_search([1,2,3,4,5], 5)) # (True, 4)
print(sequential_search([], 1)) # (False, -1)










```