def count_list(nested_list):
    count = 0
    for i in nested_list:
        if isinstance(i, list):
            count += 1
    return count

assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""
This function works by iterating over each element in the given list. If the element is a list itself, it increments the count by 1. When it has finished iterating over all the elements, it returns the count, which is the number of lists in the list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
