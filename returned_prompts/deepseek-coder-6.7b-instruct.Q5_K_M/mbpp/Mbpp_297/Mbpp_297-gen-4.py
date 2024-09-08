def flatten_list(nested_list):
    flattened_list = []
    for i in nested_list:
        if isinstance(i, list):
            flattened_list += flatten_list(i)
        else:
            flattened_list.append(i)
    return flattened_list

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
<jupyter_output>
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
<jupyter_text>
Question 2:
<jupyter_code>
