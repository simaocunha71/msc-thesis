
def common_in_nested_lists(nested_lists):
    return list(set.intersection(*map(set, nested_lists)))

print(set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])))

"""
Explanation:
The function common_in_nested_lists takes a nested list as input. 
It uses the map function to convert each inner list to a set and then finds the intersection of all these sets. 
The intersection method returns a set that contains the items that exist in all sets, which are the common elements.
"""
<jupyter_output>
{12, 18}
<jupyter_text>
Problem 4
<jupyter_code>
