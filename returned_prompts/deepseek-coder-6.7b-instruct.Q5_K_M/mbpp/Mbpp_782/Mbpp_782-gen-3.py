def odd_length_sum(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        res += ((i+1)*(n-i)+1)//2 * arr[i]
    return res

print(odd_length_sum([1,2,4]))

# 1st element: 1 * (3 - 0 + 1) // 2 * 1 = 1 * 3 // 2 * 1 = 3
# 2nd element: 2 * (3 - 1 + 1) // 2 * 2 = 2 * 3 // 2 * 2 = 3 * 2 = 6
# 3rd element: 4 * (3 - 2 + 1) // 2 * 4 = 4 * 3 // 2 * 4 = 6 * 4 = 24
# So the sum is 3 + 6 + 24 = 33

# 3rd element: 4 * (3 - 2 + 1) // 2 * 4 = 4 * 3 // 2 * 4 = 6 * 4 = 24
# So the sum is 3 + 6 + 24 = 33

"""
Explanation:
We are asked to find the sum of all subarrays of odd length.

For each element in the array, we can calculate the number of subarrays it can be part of by:
((i+1)*(n-i)+1)//2 where i is the index of the current element.

Then we multiply this number by the current element and add it to our result.

Finally, return the result.
"""
<jupyter_output>
33
<jupyter_text>
