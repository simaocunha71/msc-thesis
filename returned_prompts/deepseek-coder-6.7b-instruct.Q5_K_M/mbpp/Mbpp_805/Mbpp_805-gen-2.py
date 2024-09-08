def max_sum_list(lst):
    max_sum = 0
    max_list = []
    for sublist in lst:
        if sum(sublist) > max_sum:
            max_sum = sum(sublist)
            max_list = sublist
    return max_list

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))

# or using python's built-in function max() and key parameter
def max_sum_list(lst):
    return max(lst, key=sum)

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))
<jupyter_output>
[10, 11, 12]
[10, 11, 12]
<jupyter_text>
