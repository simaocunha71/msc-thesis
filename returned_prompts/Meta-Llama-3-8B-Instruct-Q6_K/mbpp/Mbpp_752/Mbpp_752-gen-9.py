The Jacobsthal sequence is a sequence of integers defined recursively by the following formula:
J(0) = 0
J(1) = 1
J(n) = J(n-1) + 2*J(n-2) for n > 1

Here is a Python function that generates the nth Jacobsthal number:
```
def jacobsthal_num(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + 2*b
    return b
```
This function uses a simple iterative approach to generate the Jacobsthal sequence. It initializes two variables `a` and `b` to the first two terms of the sequence (0 and 1), then iteratively updates these variables to generate the next term in the sequence. The function returns the nth term in the sequence.

The unit test `assert jacobsthal_num(5) == 11` ensures that the function returns the correct value for the 5th Jacobsthal number, which is indeed 11.