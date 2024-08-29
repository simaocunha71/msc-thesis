
def common_in_nested_lists(lists):
    common_elements = set(lists[0])
    for curr_list in lists[1:]:
        common_elements = common_elements & set(curr_list)
    return list(common_elements)

print(set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])))

"""
The function works by first converting the first list into a set of common elements. Then it goes through the remaining lists, and finds the intersection of the current list with the set of common elements. This intersection is then stored in the common_elements variable, so that it can be used in the next iteration. After going through all the lists, the function returns the common elements as a list.
"""
<jupyter_output>
{18, 12}
<jupyter_text>
Question 2
<jupyter_code>
