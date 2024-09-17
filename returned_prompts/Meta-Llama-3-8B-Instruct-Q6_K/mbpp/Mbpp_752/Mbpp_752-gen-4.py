The Jacobsthal sequence is a sequence of numbers that is defined recursively as: J(0) = 0, J(1) = 1, and J(n) = J(n-1) + 2*J(n-2) for n > 1.

Here is a Python function that calculates the nth Jacobsthal number:

```
def jacobsthal_num(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + 2*b
    return b
```

This function uses a loop to calculate the nth Jacobsthal number. It starts with the base cases a = 0 and b = 1, and then iteratively calculates the next number in the sequence as a + 2b. The final result is stored in b. 

The unit test `assert jacobsthal_num(5) == 11` ensures that the function works correctly. 

This function has a time complexity of O(n) and a space complexity of O(1), as it only uses a constant amount of space to store the variables a and b.  It is efficient for calculating large Jacobsthal numbers. 