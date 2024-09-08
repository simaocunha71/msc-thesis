
def sequential_search(array, element):
    for index in range(len(array)):
        if array[index] == element:
            return (True, index)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))

# Output: (True, 3)
<jupyter_output>
(True, 3)
<jupyter_text>
This function works by iterating over each element in the array and comparing it to the element we are looking for. If it finds a match, it returns True and the index of the match. If it doesn't find a match after checking all elements, it returns False and -1.  Binary Search Binary search is a method that allows you to quickly look up an item in a sorted list of items. This method works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.
<jupyter_code>
