def max_val(lst):
    nums = [i for i in lst if isinstance(i, (int, float))]
    return max(nums)

print(max_val(['Python', 3, 2, 4, 5, 'version']))  # Output: 5

Explanation:
The function max_val takes a list as input. It uses a list comprehension to create a new list nums that includes only the elements of the input list that are either integers or floats. The function then returns the maximum value from this new list.

This solution assumes that the heterogeneous list only contains integers or floats. If the list can also include other types of values, the function will need to be adjusted accordingly.
"""

