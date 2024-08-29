def odd_length_sum(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        result += ((i+1)*(n-i)+1)//2*arr[i]
    return result

assert odd_length_sum([1,2,4]) == 14
"""
Explanation:
The subarrays with odd lengths are: [1], [2], [4], [1, 2], [2, 4], [1, 2, 4]
The sums of these subarrays are: 1, 2, 4, 3, 6, 10
The sum of all odd length subarrays is 1 + 2 + 4 + 3 + 6 + 10 = 28
"""


