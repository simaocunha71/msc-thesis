The nth hexagonal number can be calculated using the formula: H(n) = n*(2n - 1). Here is a Python function that calculates the nth hexagonal number:

```python
def hexagonal_num(n):
    return n * (2 * n - 1)
```

This function takes an integer n as input and returns the nth hexagonal number. The unit test `assert hexagonal_num(10) == 190` ensures that the function is working correctly. The result of `hexagonal_num(10)` is indeed 190, which is the 10th hexagonal number. 

Note: The hexagonal numbers are a sequence of numbers where each term is the sum of the previous terms. This sequence starts with 1, 6, 15, 28, 45, 66, 91, 120, ... (sequence A000384 in the OEIS). The formula H(n) = n*(2n - 1) is a well-known formula for calculating the nth hexagonal number. 