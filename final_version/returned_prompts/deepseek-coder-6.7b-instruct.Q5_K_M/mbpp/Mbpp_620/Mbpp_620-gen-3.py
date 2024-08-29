
def largest_subset(lst):
    n = len(lst)
    lst.sort()
    L = [1]*n
    for i in range (1 , n):
        for j in range(0 , i):
            if lst[i] % lst[j] == 0:
                L[i] = max(L[i], L[j] + 1)
    return max(L)

print(largest_subset([ 1, 3, 6, 13, 17, 18 ])) # 4

Explanation:
The function 'largest_subset' takes an array 'lst' as input. It sorts the array and then uses dynamic programming to find the longest divisible subset. It returns the length of the largest subset.

The inner loop traverses all the previous elements of 'lst' and checks if the current element is divisible by the previous element. If it is, then it updates the length of the longest divisible subset for the current element. The result is the maximum length of the longest divisible subset among all the elements in 'lst'.
"""

