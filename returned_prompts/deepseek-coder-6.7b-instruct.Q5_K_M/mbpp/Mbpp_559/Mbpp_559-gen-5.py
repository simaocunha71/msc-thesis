def max_sub_array_sum(arr, n):
   max_so_far = arr[0]
   curr_max = arr[0]
   for i in range(1, n):
      curr_max = max(arr[i], curr_max + arr[i])
      max_so_far = max(max_so_far, curr_max)
   return max_so_far

assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7

"""
The function works by initializing two variables, max_so_far and curr_max, with the value of the first element of the array.
Then it iterates over the array, updating the value of curr_max and max_so_far in each iteration.

In each iteration, it updates the value of curr_max by comparing the current element of the array (arr[i]) with the sum of the current element and the previous value of curr_max (curr_max + arr[i]).
The maximum of these two values is stored in curr_max.

After that, it updates the value of max_so_far by comparing the current value of max_so_far with the value of curr_max.
The maximum of these two values is stored in max_so_far.

Finally, the function returns the value of max_so_far, which is the sum of the maximum contiguous sublist in the given list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
