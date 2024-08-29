def max_sub_array_sum(arr, n):

    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
        
    return max_so_far

print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))

# This is known as Kadane's Algorithm. It is used to solve the maximum subarray problem.
# The algorithm maintains a variable, max_so_far, to store the maximum sum found so far and a variable, curr_max, to store the maximum sum ending at the current position. 
# It iterates over the list and for each element, it updates curr_max to be the maximum of the current element and the sum of curr_max and the current element. 
# It then updates max_so_far to be the maximum of max_so_far and curr_max. 
# Finally, it returns max_so_far.
<jupyter_output>
7
<jupyter_text>
Question 2: Given an array of integers, return indices of the two numbers such that they add up to a specific target.You may assume that each input would have exactly one solution, and you may not use the same element twice.Example: Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
<jupyter_code>
