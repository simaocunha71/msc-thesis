
def sequential_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return (True, i)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))

# Output: (True, 3)
<jupyter_output>
(True, 3)
<jupyter_text>
Here, we are using a simple sequential search method to find the element. If the element is found, we return the boolean value True and the index position of the element. If the element is not found, we return the boolean value False and -1.  Binary Search Binary search is an algorithm that finds the position of a target value within a sorted array. It's more efficient than sequential search as it halves the array with each iteration.
<jupyter_code>
