def odd_length_sum(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        res += ((i+1)*(n-i)+1)//2 * arr[i]
    return res

print(odd_length_sum([1,2,4])) # 14

Explanation:
The idea here is to count all odd length subarrays. For each element arr[i], let's say that it is the middle element of some odd length subarray.

Consider all the subarrays that start at or before i and end at or after i. There are ((i+1)*(n-i)+1)//2 of these subarrays. If we count these subarrays as if they are all odd length, we will miss some. 

We will miss subarrays of length 1, 3, 5, ..., and we will count subarrays of length 2, 4, 6, ... multiple times.

To avoid counting subarrays of length 2, 4, 6, ... multiple times, we will count subarrays of length 1, 3, 5, ... once. 

We can get the count of subarrays of length 1 by ((i+1)*(n-i)+1)//2. We can get the count of subarrays of length 3, 5, ... by ((i+1)*(n-i)+1)//2 - ((i+1)*(n-i)-1)//2. We can get the count of subarrays of length 5, 7, ... by ((i+1)*(n-i)+1)//2 - ((i+1)*(n-i)-1)//2 - ((i+1)*(n-i)-3)//2, and so on.

Finally, we multiply the count of subarrays by the number of elements in the subarray and add the result to the total sum.

This solution works in O(n) time because we are making one pass through the array. The space complexity is O(1) because we are using a constant amount of space.
"""

# 2.
"""
