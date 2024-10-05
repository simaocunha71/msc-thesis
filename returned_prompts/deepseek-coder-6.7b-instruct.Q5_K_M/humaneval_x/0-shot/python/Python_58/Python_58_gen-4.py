

    common_elements = list(set(l1) & set(l2))
    return sorted(common_elements)


print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))


Output:


[1, 5, 653]
[2, 3]


Explanation:


In the first test, common elements are 1, 5, and 653.
In the second test, common elements are 2 and 3.
"""

# Solution 2:

"""
