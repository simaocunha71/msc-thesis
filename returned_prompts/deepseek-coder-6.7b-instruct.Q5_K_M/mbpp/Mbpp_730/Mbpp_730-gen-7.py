def consecutive_duplicates(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i - 1]]

print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]))

"""
In the function, we're creating a new list by iterating over the original list. We check if the current item is the same as the previous one. If it is, we don't add it to the new list. If it's not, we add it.
"""
<jupyter_output>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
<jupyter_text>
**Problem 2**
<jupyter_code>
