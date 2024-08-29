def sequential_search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return (True, i)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31)) # (True, 3)

"""
This function is called sequential_search and it takes two arguments, an array and an element. The function goes through each element in the array in order, comparing it to the element being searched for. If a match is found, it returns a tuple containing True and the index of the match. If no match is found after going through all elements in the array, it returns False and -1.
"""
<jupyter_output>
(True, 3)
<jupyter_text>
Question 2:
<jupyter_code>
