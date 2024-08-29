def sequential_search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return (True, i)
    return (False, -1)

# Test the function
print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))  # (True, 3)

"""
Explanation:

The function sequential_search takes in an array and an element. It iterates through the array from the beginning to the end. When it finds the element, it immediately returns a tuple containing True and the index of the element. If the function does not find the element after going through the entire array, it returns a tuple containing False and -1.
"""
<jupyter_output>
(True, 3)
<jupyter_text>
Question 2
<jupyter_code>
