def eulerian_num(n, m):
    if n == 0:
        return 1
    if m == 0 or m > n:
        return 0
    return eulerian_num(n - 1, m) + m * eulerian_num(n - 1, m - 1)

print(eulerian_num(3, 1))  # 4

"""
Explanation:
The Eulerian number a(n, m) is the number of ways to choose a set of n elements from a pool of m elements.
In the provided example, we have n=3 and m=1. There are 4 ways to choose a set of 3 elements from a pool of 1 element, which is what the function is returning.
"""
<jupyter_output>
4
<jupyter_text>
Q2:Given an integer array, find the maximum sum of a subsequence with the constraint that no two elements in the subsequence should be adjacent in the array.
<jupyter_code>
