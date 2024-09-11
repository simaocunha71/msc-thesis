```
def eulerian_num(n, m):
    """
    >>> eulerian_num(3, 1)
    4
    """
    # Your code here
    if n == 0:
        return 0 if m == 0 else 1
    if m == 0:
        return 0
    return eulerian_num(n-1, m) + eulerian_num(n-1, m-1) + (n-m) * eulerian_num(n-1, m-1)
```

B:
In the eulerian_num function, the recursion is based on the Eulerian numbers, which are defined as follows:

For any fixed positive integer n, the Eulerian number e(n, m), where 0 ≤ m ≤ n, is defined to be the number of permutations of the first m + 1 elements of a set of n + 1 elements, each of which contains exactly m + 1 elements in increasing order.

The Eulerian numbers are defined by the following recurrence relation:

e(n, m) = e(n-1, m) + e(n-1, m-1) + (n-m) * e(n-1, m-1)

with the boundary conditions e(n, 0) = 0 if n > 0, and e(0, 0) = 1.

To find the Eulerian number e(n, m), we can use the following steps:

1. If n is 0, return 0 if m is 0, otherwise return 1. This is because there are no elements in the set, so there are no permutations.

2. If m is 0, return 0. This is because there are no permutations of the first m + 1 elements.

3. Otherwise, we can use the recurrence relation to compute e(n, m):

   e(n, m) = e(n-1, m) + e(n-1, m-1) + (n-m) * e(n-1, m-1)

4. The base case for the recurrence relation is e(0, 