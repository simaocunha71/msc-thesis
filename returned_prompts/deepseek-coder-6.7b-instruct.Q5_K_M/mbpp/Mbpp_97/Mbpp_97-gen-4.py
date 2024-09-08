def frequency_lists(lst):
    result = {}
    for sublist in lst:
        for item in sublist:
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
    return result

# Test
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
Explanation:
We iterate over each sublist and then each item in each sublist. If an item is already in the result dictionary, we increment its count by 1, if not, we add it to the dictionary with a count of 1.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 5
<jupyter_code>
