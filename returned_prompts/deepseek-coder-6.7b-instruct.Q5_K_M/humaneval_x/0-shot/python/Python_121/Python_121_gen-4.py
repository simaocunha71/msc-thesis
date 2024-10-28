
    return sum(el for i, el in enumerate(lst) if i % 2 == 0 and el % 2 != 0)

Test cases:

print(solution([5, 8, 7, 1])) #==> 12
print(solution([3, 3, 3, 3, 3])) #==> 9
print(solution([30, 13, 24, 321])) #==>0

The function works by iterating over each element in the list along with its index. The condition `i % 2 == 0 and el % 2 != 0` checks if the element is in an even position and is odd. If true, the element is added to the sum.
"""

# Solution 2:

"""
