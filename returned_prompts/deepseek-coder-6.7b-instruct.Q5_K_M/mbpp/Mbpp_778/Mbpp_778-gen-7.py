def pack_consecutive_duplicates(lst):
    result = []
    current_sublist = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            current_sublist.append(lst[i])
        else:
            result.append(current_sublist)
            current_sublist = [lst[i]]
    result.append(current_sublist)
    return result

print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
<jupyter_output>
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
<jupyter_text>
Question 2:
<jupyter_code>
