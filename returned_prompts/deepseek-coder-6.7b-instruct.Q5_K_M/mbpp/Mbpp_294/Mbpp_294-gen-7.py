def max_val(lst):
    max_value = None
    for i in lst:
        if isinstance(i, int) or isinstance(i, float):
            if max_value is None or i > max_value:
                max_value = i
    return max_value

print(max_val(['Python', 3, 2, 4, 5, 'version']))  # Output: 5

# In this function, we iterate over the list. If an item is an integer or a float, we compare it with the current max_value. If the item is greater, we update max_value. At the end, we return max_value which will be the maximum integer or float in the list. If the list does not contain any integers or floats, the function will return None.
<jupyter_output>
5
<jupyter_text>
**Question 2**
<jupyter_code>
