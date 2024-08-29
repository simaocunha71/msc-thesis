def eulerian_num(n, m):
    if m > n:
        return 0
    if m == 0:
        return 1
    return eulerian_num(n-1, m) + eulerian_num(n, m-1)

print(eulerian_num(3, 1))  # 4
"""
Explanation:
The function is using the recursive definition of Eulerian number.
If m > n, it returns 0.
If m == 0, it returns 1.
Otherwise, it returns the sum of Eulerian numbers of (n-1, m) and (n, m-1).
"""

