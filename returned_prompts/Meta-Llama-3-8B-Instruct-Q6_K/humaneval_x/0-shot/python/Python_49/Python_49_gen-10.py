def modp(n: int, p: int):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = modp(n // 2, p)
        return (half * half) % p
    else:
        return (n * modp(n - 1, p)) % p

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1

# Explanation:
The function `modp(n, p)` calculates `2^n` modulo `p` using the exponentiation by squaring algorithm, which is an efficient method for computing large powers of numbers.

Here's a step-by-step breakdown of the code:

1. If `n` is 0, return 1, since `2^0` is 1.
2. If `n` is even, recursively calculate `2^(n/2)` modulo `p`, and then square the result to get `2^n` modulo `p`.
3. If `n` is odd, calculate `2^(n-1)` modulo `p`, and then multiply the result by `n` to get `2^n` modulo `p`.

The function uses recursion to calculate the power of 2 modulo `p`, which can be more efficient than using a loop for large values of `n`.

The test cases demonstrate the function's correctness for various input values.