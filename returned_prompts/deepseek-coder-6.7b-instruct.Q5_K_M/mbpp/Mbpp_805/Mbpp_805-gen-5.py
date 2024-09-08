def max_sum_list(l):
    max_sum = 0
    max_list = []
    for sub_list in l:
        if sum(sub_list) > max_sum:
            max_sum = sum(sub_list)
            max_list = sub_list
    return max_list

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))
<jupyter_output>
[10, 11, 12]
<jupyter_text>
**Q2**
<jupyter_code>
