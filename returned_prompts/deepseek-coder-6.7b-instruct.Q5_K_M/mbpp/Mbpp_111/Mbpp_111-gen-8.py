def common_in_nested_lists(lst):
    common = set(lst[0])
    for l in lst[1:]:
        common = common & set(l)
    return list(common)

print(set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])))
<jupyter_output>
{12, 18}
<jupyter_text>
