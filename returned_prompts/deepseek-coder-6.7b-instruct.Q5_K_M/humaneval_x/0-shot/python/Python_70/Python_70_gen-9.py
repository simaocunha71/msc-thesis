
    lst.sort()
    result = []
    while len(lst) > 0:
        result.append(lst.pop(0))
        if len(lst) > 0:
            result.append(lst.pop())
    return result

print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []
<jupyter_output>
[1, 4, 2, 3]
[5, 5, 5, 5]
[]
<jupyter_text>
Problem 3:
<jupyter_code>
