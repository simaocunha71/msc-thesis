
def consecutive_duplicates(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]

print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]))

"""
This function uses list comprehension to iterate over the input list and adds an element to the new list only if it is the first element of the list or it is different from the previous one.
"""
<jupyter_output>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
<jupyter_text>
