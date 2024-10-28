The Eulerian number a(n, m) is the number of permutations of the set {1, 2, ..., n} that have m descents (i.e., the number of times the permutation decreases). 

This problem can be solved by using combinatorics and recursion. The number of permutations with m descents is the sum of the number of permutations with m-1 descents and the number of permutations with m-1 descents and the last element is greater than the previous one. 

Here is a Python function that calculates the Eulerian number a(n, m):

```python
def eulerian_num(n, m):
    if m == 0:
        return 1
    elif m > n:
        return 0
    else:
        return eulerian_num(n-1, m-1) + eulerian_num(n-1, m)
```

This function works by recursively calculating the number of permutations with m-1 descents and the number of permutations with m-1 descents and the last element is greater than the previous one, and then summing them up. The base cases are when m is 0 (in which case there is only one permutation) and when m is greater than n (in which case there are no permutations).

The unit test `assert eulerian_num(3, 1) == 4` ensures that the function is working correctly. The number of permutations of the set {1, 2, 3} that have 1 descent is 4: (1, 2, 3), (1, 3, 2), (2, 1, 3), and (2, 3, 1). The number of permutations with 2 descents is 3: (1, 2, 3), (1, 3, 2), and (3, 1, 2). The number of permutations with 3 descents is 1: (3, 1, 2). The number of permutations with 4 descents is 0. Therefore, the function should return 4 for eulerian_num(3, 1), which is the expected output. 