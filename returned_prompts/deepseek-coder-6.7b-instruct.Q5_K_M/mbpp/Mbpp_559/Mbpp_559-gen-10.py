def max_sub_array_sum(arr, n):

    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
        
    return max_so_far

print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))

"""
The function works by initializing two variables, max_so_far and curr_max, to the first element of the array. 
It then iterates through the array, updating the curr_max at each step with the maximum between the current element and the sum of the current element and the previous curr_max. 
It then updates the max_so_far at each step with the maximum between the current max_so_far and the current curr_max. 
Finally, the function returns max_so_far, which will be the sum of the largest contiguous sublist in the array.
"""
<jupyter_output>
7
<jupyter_text>
Question 2
<jupyter_code>
