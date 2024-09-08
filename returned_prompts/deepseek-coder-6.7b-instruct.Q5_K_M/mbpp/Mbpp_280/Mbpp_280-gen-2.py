def sequential_search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return (True, i)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))

"""
This function works by iterating through the given array. If the current element in the array matches the element we are searching for, we return a tuple containing True and the current index. If the loop completes without finding the element, we return a tuple containing False and -1.
"""

"""
This is an example of a linear search, as it checks each element in order. The time complexity of this search is O(n), which is the best case scenario because in the worst case scenario it must check all elements.
"""

"""
Testing with different cases:
"""

print(sequential_search([11,23,58,31,56,77,43,12,65,19],19)) # Expected output (True, 9)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],78)) # Expected output (False, -1)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],11)) # Expected output (True, 0)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],43)) # Expected output (True, 6)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],65)) # Expected output (True, 8)
<jupyter_output>
(True, 3)
(True, 9)
(True, 0)
(True, 6)
(