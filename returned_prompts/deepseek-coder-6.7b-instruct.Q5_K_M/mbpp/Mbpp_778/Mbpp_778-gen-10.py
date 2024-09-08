def pack_consecutive_duplicates(lst):
    res = []
    temp = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            temp.append(lst[i])
        else:
            res.append(temp)
            temp = [lst[i]]
    res.append(temp)
    return res

print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))

# Output: [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

"""
The function works by iterating over the list and comparing each element with the previous one. 
If they are the same, it adds the element to a temporary list. If they are different, it adds the temporary list to the result and starts a new temporary list with the current element.
Finally, it adds the last temporary list to the result.
"""
<jupyter_output>
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
<jupyter_text>
2. Write a Python function to find the largest number in a list.
<jupyter_code>
