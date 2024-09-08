
def count_Pairs(l: list, n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if l[i] != l[j]:
                count += 1
    return count


assert count_Pairs([1,2,1],3) == 2

"""
Explanation:
The function counts the number of unordered pairs in the list.
For each pair, it checks if both elements are unequal. If they are, it increments the count.
Finally, it returns the count.
"""

# 2) Write a Python function that takes a list of integers and returns the maximum possible sum of two distinct elements.
# If the list is empty or has fewer than two elements, the function should return None.


