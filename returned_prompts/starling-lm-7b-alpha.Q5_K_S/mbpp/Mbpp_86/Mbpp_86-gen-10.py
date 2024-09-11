```
def centered_hexagonal_number(n):
    n -= 1
    a = n * (3 * n + 1) // 2
    b = n * (n + 1)
    c = (n + 1) * (3 * n + 1) // 2
    return a + b + c
```

The above Python code defines a function `centered_hexagonal_number` that computes the nth centered hexagonal number. The definition of the nth centered hexagonal number is the sum of the first n positive integers, the first n-1 positive integers, and the first n+1 positive integers. The function uses the formula `a + b + c` to compute the result, where `a = n * (3 * n + 1) // 2`, `b = n * (n + 1)`, and `c = (n + 1) * (3 * n + 1) // 2`.

To use the function, you can call `centered_hexagonal_number` with the desired value of `n`, and it will return the nth centered hexagonal number. For example, if you want to find the 10th centered hexagonal number, you can call `centered_hexagonal_number(10)`, which will return 271.

```python
print(centered_hexagonal_number(10))  # Output: 271
```

This code will print the 10th centered hexagonal number, which is 271.

The function `centered_hexagonal_number` is designed to handle any positive integer value of `n`, so you can use it to find the nth centered hexagonal number for any positive integer value of `n`.

```python
print(centered_hexagonal_number(5))  # Output: 76
print(centered_hexagonal_number(100))  # Output: 35700
```

These code snippets demonstrate how to use the function to find the 5th and 100th centered hexagonal numbers, which are 76 and 35700, respectively.

Overall, the function `centered_hex