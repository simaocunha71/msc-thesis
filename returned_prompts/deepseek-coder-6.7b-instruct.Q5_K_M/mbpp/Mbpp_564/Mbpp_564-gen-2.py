def count_Pairs(lst, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_Pairs([1,2,1], 3))  # Output: 2

Explanation:
The function counts the number of unordered pairs where both elements are unequal. It does this by iterating through each element in the list (lst) and comparing it with each subsequent element (j). If the elements are not equal, it increments the count. The function finally returns the count.

Note: This solution assumes the list and number of elements (n) are given as input.
"""

# Task 2:

"""
