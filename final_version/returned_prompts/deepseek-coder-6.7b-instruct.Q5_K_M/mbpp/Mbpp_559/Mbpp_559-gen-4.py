def max_sub_array_sum(arr, size):
    max_so_far = arr[0]
    curr_max = arr[0]
 
    for i in range(1, size):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
        
    return max_so_far

# Test
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_sub_array_sum(arr, len(arr)))
<jupyter_output>
7
<jupyter_text>
ExplanationThe function `max_sub_array_sum` uses the Kadane's algorithm to find the sum of the largest contiguous sublist. The idea is to look for all positive contiguous segments of the array (max_ending_here is used for this). And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this). Each time when we get a positive sum we compare it with max_so_far and update max_so_far if it is greater than max_so_far.  Exercise 2: Implement a function to find the maximum product sublist
<jupyter_code>
