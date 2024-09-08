
def common_in_nested_lists(lists):
    return list(set.intersection(*map(set, lists)))

print(set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])))
<jupyter_output>
{18, 12}
<jupyter_text>
Q2:
<jupyter_code>
