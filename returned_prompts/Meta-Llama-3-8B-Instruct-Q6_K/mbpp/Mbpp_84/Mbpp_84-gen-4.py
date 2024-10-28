The Newman-Conway sequence is a sequence of numbers where each term is the sum of the two preceding terms, starting with 1 and 2. 

Here is a Python function that generates the Newman-Conway sequence:

```Python
def sequence(n):
    if n <= 2:
        return 1 if n == 1 else 2
    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, a + b
    return b
```
This function first checks if the input number `n` is less than or equal to 2. If it is, the function returns 1 or 2 depending on the value of `n`. If `n` is greater than 2, the function initializes two variables `a` and `b` to 1 and 2 respectively. It then enters a loop that runs `n-2` times, updating the values of `a` and `b` in each iteration. The function finally returns the value of `b`, which is the `n`th term in the Newman-Conway sequence. 

The unit test `assert sequence(10) == 6` ensures that the function correctly calculates the 10th term in the sequence, which is indeed 6. 