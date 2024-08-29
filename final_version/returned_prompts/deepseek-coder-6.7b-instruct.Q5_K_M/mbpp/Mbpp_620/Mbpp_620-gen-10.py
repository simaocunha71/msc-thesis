
def largest_subset(arr):
    arr.sort()
    n = len(arr)
    subset = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i]%arr[j] == 0 and subset[i]<subset[j]+1:
                subset[i] = subset[j]+1
    maximum = 0
    for i in range(len(subset)):
        maximum = max(maximum, subset[i])
    return maximum

print(largest_subset([1, 3, 6, 13, 17, 18]))

"""
Explanation:
In the given list [1, 3, 6, 13, 17, 18] the subsets that meet the condition are [1, 3, 6, 18] and [1, 3, 13, 18]. 
So the size of the largest subset is 4.
"""

# Time complexity: O(n^2)
# Space complexity: O(n)

# Note: This solution assumes that the list of numbers is not empty and contains positive integers only.
# It's also worth mentioning that this solution may not work for lists with negative numbers as it considers only divisibility.
<jupyter_output>
4
<jupyter_text>
Q2:
<jupyter_code>
