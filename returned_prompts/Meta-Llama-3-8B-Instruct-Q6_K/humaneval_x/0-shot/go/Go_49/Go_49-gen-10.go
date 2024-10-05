The function `Modp(n, p)` calculates `2^n` modulo `p` and returns the result. The function is designed to handle large values of `n` and `p` efficiently.

Here is the implementation:
```python
def Modp(n, p):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = Modp(n // 2, p)
        return (half * half) % p
    else:
        half = Modp((n - 1) // 2, p)
        return (half * half * 2) % p
```
Here's how the function works:

1. If `n` is 0, the function returns 1, since `2^0` is 1.
2. If `n` is even, the function calculates `2^(n/2)` modulo `p` using the recursive formula `2^n = (2^(n/2))^2` modulo `p`. This reduces the problem size by half.
3. If `n` is odd, the function calculates `2^((n-1)/2)` modulo `p` using the recursive formula `2^n = (2^((n-1)/2))^2 * 2` modulo `p`. This reduces the problem size by half.
4. The function uses the modulo operator `%` to ensure that the result is within the range `[0, p)`.

The function is designed to handle large values of `n` and `p` efficiently by recursively reducing the problem size by half. This makes the function suitable for large inputs.

You can test the function with the examples provided in the original problem statement:
```python
print(Modp(3, 5))  # Output: 3
print(Modp(1101, 101))  # Output: 2
print(Modp(0, 101))  # Output: 1
print(Modp(3, 11))  # Output: 8
print(Modp(100, 101))  # Output: 1
```
I hope this helps! Let me know if you have any questions or need further clarification.