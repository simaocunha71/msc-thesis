def consecutive_duplicates(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]

print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

Explanation:
The function `consecutive_duplicates` takes a list `lst` as input and returns a new list that contains only the first occurrence of each consecutive duplicate. This is done by iterating through `lst` and adding each element to the new list if it is not the same as the previous element.

The condition `i == 0 or lst[i] != lst[i-1]` is used to check if the current element is the first element of the list (`i == 0`) or if it is different from the previous element (`lst[i] != lst[i-1]`). Only the first occurrence of each consecutive duplicate is kept.

The function returns this new list.

So, when you call `consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])`, it returns `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]`.

This is because `0` is repeated, but only the first occurrence is kept, `0` is replaced by `1`, `4` is repeated, but only the first occurrence is kept, and so on.

Note: This function works by checking each element against the previous one, so it will not remove all consecutive duplicates if there are more than two consecutive duplicates.
"""
<jupyter_output>
<empty