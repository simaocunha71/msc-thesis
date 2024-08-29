def odd_length_sum(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans += ((i+1)*(n-i)+1)//2 * arr[i]
    return ans

print(odd_length_sum([1,2,4])) # 14

Explanation:
For each index i in the array, we calculate the number of odd length subarrays that include arr[i] and then multiply it with arr[i].
The number of odd length subarrays that include arr[i] is ((i+1)*(n-i)+1)//2. This is based on the fact that for each arr[i], there are (i+1)*(n-i) subarrays and we need to add 1 for the subarray that includes only arr[i].
Finally, we sum up all the results to get the answer.
"""

"""
