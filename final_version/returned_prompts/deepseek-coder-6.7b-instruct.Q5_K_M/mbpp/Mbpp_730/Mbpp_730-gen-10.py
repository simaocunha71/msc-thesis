def consecutive_duplicates(lst):
    res = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            res.append(lst[i])
    return res

print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]))

#Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

"""
This function works by iterating over the given list and adding each element to the result list if it is not equal to the previous one. This means that any consecutive duplicates will be removed from the result list.
"""

"""
This function has a time complexity of O(n), where n is the length of the list, because it needs to iterate over the list once.
"""

"""
This function has a space complexity of O(n), where n is the length of the list, because it creates a new list that is the same size as the input list in the worst case scenario.
"""
<jupyter_output>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
<jupyter_text>
Question 3
<jupyter_code>
