
def largest_subset(lst):
    lst.sort()
    dp = [1]*len(lst)
    for i in range(len(lst)):
        for j in range(i):
            if lst[i]%lst[j] == 0:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(largest_subset([ 1, 3, 6, 13, 17, 18 ])) # Output: 4

Explanation:
The largest subset of a list of numbers so that every pair is divisible is [1, 3, 6, 18] because 1, 3, 6 and 18 are all divisible by 1, 3, 6 and 18 respectively.
"""

