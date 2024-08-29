def max_sub_array_sum(lst, n):
    max_sum = 0
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += lst[j]
            max_sum = max(sum_, max_sum)
    return max_sum

print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))


"""
Kadane's algorithm:
"""

def max_sub_array_sum(lst):
    curr_sum = max_sum = lst[0]
    for num in lst[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3]))
"""

Output:
7
7
"""

