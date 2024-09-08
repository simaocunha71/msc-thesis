
def largest_subset(lst):
    lst.sort()
    n = len(lst)
    subset = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if lst[i]%lst[j] == 0 and subset[i]<subset[j]+1:
                subset[i] = subset[j]+1
    maximum = 0
    for i in range(len(subset)):
        maximum = max(maximum, subset[i])
    return maximum

print(largest_subset([ 1, 3, 6, 13, 17, 18 ])) # Output: 4

Explanation:
The largest subset of a list of numbers so that every pair is divisible is [1, 3, 6, 18]. They are all divisible by 1, 3, 2 and 1 respectively.
"""

