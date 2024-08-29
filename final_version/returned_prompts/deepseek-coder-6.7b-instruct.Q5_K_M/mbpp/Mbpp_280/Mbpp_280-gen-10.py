def sequential_search(arr, elm):
    for i in range(len(arr)):
        if arr[i] == elm:
            return (True, i)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))
<jupyter_output>
(True, 3)
<jupyter_text>
**Binary Search**
<jupyter_code>
