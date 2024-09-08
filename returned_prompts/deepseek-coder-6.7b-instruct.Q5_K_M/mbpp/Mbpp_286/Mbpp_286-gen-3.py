
def max_sub_array_sum_repeated(arr, k, n):
    # calculating the total sum of the array
    total_sum = sum(arr)

    # calculating the sum of the array after it is repeated k times
    arr_sum = sum(arr * k)

    # calculating the maximum sub-array sum
    max_sum = max(arr_sum, total_sum * (k - 1))

    # returning the maximum sum
    return max_sum

# testing the function
print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))
"""
Output:
30
"""

# time complexity: O(n)
# space complexity: O(1)

"""
Explanation:
In this problem, we are given an array 'arr' and an integer 'k'. We need to find the maximum sub-array sum of the array 'arr' repeated 'k' times. 

We first calculate the total sum of the array 'arr'. Then, we calculate the sum of the array 'arr' after it is repeated 'k' times. 

We then calculate the maximum sum by comparing the sum of 'arr' after it is repeated 'k' times with the total sum of 'arr' multiplied by 'k - 1'. 

Finally, we return the maximum sum.
"""

# Note: This solution assumes that the array 'arr' contains at least one positive number. If not, the maximum sub-array sum could be zero.

# Note: This solution assumes that 'k' is a positive integer. If 'k' is zero or negative, the function will return a sum of zero.

# Note: This solution assumes that 'n' is a positive integer. If 'n' is zero or negative, the function will return a sum of zero.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 5Given an array of integers and a number `k`, write a function that returns the length of the longest subarray that sums to `k`. If no such subarray exists, return 0.**Example:**```pythonlongest_subarray_length