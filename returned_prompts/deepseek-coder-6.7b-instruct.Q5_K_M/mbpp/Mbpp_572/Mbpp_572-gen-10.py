def two_unique_nums(nums_list):
    return list(set(numnums_list))

print(two_unique_nums([1,2,3,2,3,4,5]))

"""
This function works by converting the input list to a set, which automatically removes duplicates because sets can only contain unique elements. The function then converts the set back to a list and returns it.
"""
<jupyter_output>
[1, 2, 3, 4, 5]
<jupyter_text>
1.6. Write a Python function to sort a list of tuples by the second element of each tuple.
<jupyter_code>
