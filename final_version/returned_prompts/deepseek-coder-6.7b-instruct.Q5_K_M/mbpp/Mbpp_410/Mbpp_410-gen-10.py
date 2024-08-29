def min_val(lst):
    min_num = None
    for item in lst:
        if isinstance(item, int):
            if min_num is None or item < min_num:
                min_num = item
    return min_num

print(min_val(['Python', 3, 2, 4, 5, 'version']))

# Output: 2

"""
This function works by iterating over the list and checking if each item is an integer. If it is, it checks if it is less than the current minimum. If it is, it updates the minimum. The function then returns the minimum integer found. If no integer is found, it returns None.
"""
<jupyter_output>
2
<jupyter_text>
Question 2
<jupyter_code>
"""
