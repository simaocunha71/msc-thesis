def max_sub_array_sum(arr, n):
    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8)) # 7

"""
Explanation:

The function uses Kadane's algorithm to solve this problem.

The algorithm maintains two variables, `curr_max` and `max_so_far`.
- `curr_max` tracks the maximum sum of the sublist ending at the current position.
- `max_so_far` tracks the overall maximum sublist sum found so far.

During each iteration, the `curr_max` is updated to be the maximum of the current element and the sum of the current element and `curr_max`.
Then `max_so_far` is updated to be the maximum of `max_so_far` and `curr_max`.

After all iterations, `max_so_far` will hold the sum of the largest contiguous sublist.

The time complexity of the algorithm is O(n), where n is the size of the input list.
"""
<jupyter_output>
7
<jupyter_text>
Question 2
<jupyter_code>
