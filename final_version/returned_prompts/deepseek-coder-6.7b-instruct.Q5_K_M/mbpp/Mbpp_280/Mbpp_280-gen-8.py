def sequential_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return (True, i)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))



