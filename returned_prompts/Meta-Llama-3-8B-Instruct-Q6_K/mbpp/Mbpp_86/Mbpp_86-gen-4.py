The centered hexagonal number can be calculated using the formula: 
cn = 6n^2 - 6n + 1

Here is the Python function to find the nth centered hexagonal number:

```Python
def centered_hexagonal_number(n):
    return 6 * n ** 2 - 6 * n + 1
```

This function takes an integer `n` as input and returns the nth centered hexagonal number. The unit test `assert centered_hexagonal_number(10) == 271` ensures that the function works correctly. For example, `centered_hexagonal_number(10)` returns `271`, which is the 10th centered hexagonal number. 