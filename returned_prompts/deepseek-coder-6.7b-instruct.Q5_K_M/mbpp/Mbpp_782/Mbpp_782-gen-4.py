def odd_length_sum(arr):
    sum_val = 0
    n = len(arr)
    for i in range(n):
        sum_val += ((i+1)*(n-i)+1)//2 * arr[i]
    return sum_val

print(odd_length_sum([1,2,4]))

# The function works by iterating through each element in the array, then multiplying the count of subarrays containing that element with the value of that element. 
# The count of subarrays containing element at index i is ((i+1)*(n-i)+1)//2.

# For example, if we have arr = [1,2,4], the function will return the sum of the following:
# 1 appears in 1 subarray ([1])
# 2 appears in 3 subarrays ([2], [1, 2, 4], [2, 4])
# 4 appears in 1 subarray ([4])
# So, the sum is 1 + 2*2 + 4*1 = 1 + 4 + 4 = 14.
<jupyter_output>
14
<jupyter_text>
**Problem 3**
<jupyter_code>
