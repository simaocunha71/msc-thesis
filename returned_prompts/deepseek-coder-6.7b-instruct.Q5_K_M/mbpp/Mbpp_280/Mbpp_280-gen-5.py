def sequential_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return True, i
    return False, -1

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))

# Output: (True, 3)

"""
In the above code, we define a function 'sequential_search' that takes an array and an element as arguments. We then iterate over the array. If we find the element, we return a tuple with True and the index of the element. If we don't find the element, we return False and -1.

When we call the function with the given inputs, we get the expected output.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Binary Search
<jupyter_code>
"""
