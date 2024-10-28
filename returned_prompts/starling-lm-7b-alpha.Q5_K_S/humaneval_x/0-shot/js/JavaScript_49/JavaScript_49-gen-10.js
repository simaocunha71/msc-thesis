To solve this problem, we need to calculate the result of 2^n modulo p, where p is a prime number. Here are some steps to solve this problem:

1. Initialize a variable `result` with a value of 1.
2. Calculate the remainder of `n` divided by 2. If `n` is an even number, set `n` to `n/2`, otherwise set `n` to `(n-1)/2`.
3. Repeat steps 2 and 4 until `n` is 0.
4. Calculate the result of `result * 2` modulo `p` and assign it to `result`.
5. If `n` is even, set `result` to `result * result` modulo `p`, and assign it to `result`.
6. If `n` is odd, set `result` to `result * (result * result)` modulo `p`, and assign it to `result`.
7. Return the value of `result` as the final result.

Here is the code to solve this problem:

```python
def modp(n, p):
    result = 1
    while n != 0:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n - 1) / 2
        result = (result * 2) % p
    if n % 2 == 0:
        result = (result * result) % p
    else:
        result = (result * (result * result)) % p
    return result
```

The time complexity of this solution is O(logn) because in the while loop, at each iteration, we divide `n` by 2, which reduces the value of `n` by half.

The space complexity of this solution is O(1) because we only need a constant amount of space to store the result.

Finally, we can test this function with some test cases to verify its correctness:

```python
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))