def eulerian_num(n, m):
    if m == 0:
        return 1
    elif n == 0:
        return 0
    else:
        return (m * eulerian_num(n - 1, m) + eulerian_num(n, m - 1))

print(eulerian_num(3, 1))

# 4
"""
Explanation:
The Eulerian number a(n, m) is a generalization of the binomial coefficient. It counts the number of permutations of n elements, where m maximum runs have length greater than 1.
For example, a(3, 1) is 4 because there are 4 permutations of 3 elements: {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}.
"""

# 2.
