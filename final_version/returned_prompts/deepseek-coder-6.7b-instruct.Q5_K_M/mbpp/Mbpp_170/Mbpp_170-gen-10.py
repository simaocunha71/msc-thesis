def sum_range_list(l, start_index, end_index):
    return sum(l[start_index:end_index+1])

print(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10))

# Solution: 29

# Alternative solution using for loop
def sum_range_list_v2(l, start_index, end_index):
    sum_val = 0
    for i in range(start_index, end_index+1):
        sum_val += l[i]
    return sum_val

print(sum_range_list_v2([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10))

# Solution: 29
<jupyter_output>
29
29
<jupyter_text>
Problem 4Given a list of strings, return a list of the strings, sorted first by the number of distinct characters they have and then by their length.
<jupyter_code>
