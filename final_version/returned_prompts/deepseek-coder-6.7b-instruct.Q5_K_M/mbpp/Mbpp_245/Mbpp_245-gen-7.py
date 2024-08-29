"""
This problem can be solved by using dynamic programming. 

Firstly, we will find the increasing subsequence sum array. 
Then, we will find the decreasing subsequence sum array. 
Finally, we will sum up the maximum sum of bitonic subsequence from increasing and decreasing sum array.

We will use Python to solve this problem.
"""

def max_sum(arr):
    n = len(arr)
    if n < 3:
        return 0
    
    # Initialize the increasing and decreasing sum array with the input array.
    inc = arr[:]
    dec = arr[:]
    
    # Find the maximum sum of increasing subsequence.
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]
    
    # Find the maximum sum of decreasing subsequence.
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]
    
    # Find the maximum sum of bitonic subsequence.
    bitonic = [0]*n
    for i in range(n):
        bitonic[i] = inc[i] + dec[i] - arr[i]
    
    return max(bitonic)

print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]))

"""
Output:
194

Explanation:
The maximum sum bitonic subsequence is 180 which is obtained by taking the increasing subsequence [1, 15, 51, 100] and the decreasing subsequence [100, 18, 9].
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(n)