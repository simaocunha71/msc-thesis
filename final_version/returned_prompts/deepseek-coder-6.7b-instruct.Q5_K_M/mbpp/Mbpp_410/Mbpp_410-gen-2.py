def min_val(lst):
    return min([i for i in lst if isinstance(i, int)])

print(min_val(['Python', 3, 2, 4, 5, 'version']))

# Output: 2

"""
This function works by using a list comprehension to create a new list that only includes the integers from the original list. It then uses the built-in min() function to find the minimum value in this new list.
"""
<jupyter_output>
2
<jupyter_text>
Exercise 2
<jupyter_code>
