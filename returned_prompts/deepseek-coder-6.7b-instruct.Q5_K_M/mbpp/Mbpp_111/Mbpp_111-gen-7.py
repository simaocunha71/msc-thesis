
def common_in_nested_lists(nested_lists):
    if len(nested_lists) == 0:
        return []
    common_elements = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common_elements = common_elements.intersection(set(lst))
    return list(common_elements)

print(set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])))

assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
<jupyter_output>
{18, 12}
<jupyter_text>
Question 2:
<jupyter_code>
