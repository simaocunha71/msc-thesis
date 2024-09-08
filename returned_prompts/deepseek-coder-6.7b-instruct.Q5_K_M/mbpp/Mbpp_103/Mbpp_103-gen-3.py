def eulerian_num(n, m):
    if m == 0:
        return 1
    elif n < m:
        return 0
    else:
        return eulerian_num(n - 1, m) + eulerian_num(n, m - 1)

print(eulerian_num(3, 1))  # 4
"""
Explanation:
The Eulerian number a(n, m) counts the number of ways to partition a set of n labeled objects into m non-empty unlabelled subsets.
The function recursively calculates the Eulerian number by summing the ways to partition the set into m subsets (a(n, m - 1)) and the ways to partition a set of n labeled objects into m non-empty unlabelled subsets (a(n - 1, m)).
"""

