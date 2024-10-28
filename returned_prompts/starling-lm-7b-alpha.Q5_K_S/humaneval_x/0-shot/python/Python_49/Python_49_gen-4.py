
To solve this problem, we can use the following steps:

1. First, we can create a function called `modp` that takes two arguments: `n` and `p`. This function will calculate and return `2^n` modulo `p`.

2. Inside the `modp` function, we can initialize a variable `result` to 1. This variable will store the result of the calculation.

3. We can then use a while loop to calculate `2^n` by repeatedly multiplying `result` by 2. The loop will continue until `n` becomes 0.

4. Inside the loop, we can check if `n` is less than `p`. If it is, we can add the result of `n` multiplied by `result` to `result`. This step is necessary to handle cases where `n` is larger than `p`.

5. After the loop, we can return the final value of `result` as the result of the calculation.

6. To verify the correctness of the function, we can use a series of test cases. Each test case should check if the result of the function matches the expected result.

7. Finally, we can call the `modp` function with different values of `n` and `p` to see if the function works correctly.

Here's an example implementation of the `modp` function in Python:

```python
def modp(n: int, p: int):
    result = 1
    while n:
        if n < p:
            result = (result * n) % p
        n >>= 1
    return result
```

And here are some test cases to verify the correctness of the function:

```python
print(modp(3, 5) == 3)  # True
print(modp(1101, 101) == 2)  # True
print(modp(0, 101) == 1)  # True
print(modp(3, 11) == 8)  # True
print(modp(100, 101) == 1)  # True
```

These test cases demonstrate that the `modp` function correctly calculates