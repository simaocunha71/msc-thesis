def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
<jupyter_output>
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
<jupyter_text>
Question 2
<jupyter_code>
