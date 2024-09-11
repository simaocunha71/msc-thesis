```
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result
```

Explanation:
The function `power` takes two arguments, `a` and `b`. It initializes a variable `result` to 1. Then, it enters a loop that repeats `b` times. In each iteration of the loop, the value of `result` is multiplied by the value of `a`. After the loop finishes, the final value of `result` is returned as the result of the function. The provided assertion `power(3,4) == 81` confirms that the function correctly calculates the value of `a` to the power `b` when `a` is 3 and `b` is 4, which is indeed 81.

In the provided solution, the function `power` uses a simple loop to calculate the power of `a` by repeatedly multiplying `a` by itself `b` times. This approach is straightforward and efficient, as it only requires a single loop to perform the calculation.

It's worth mentioning that there are other ways to calculate the power of a number, such as using exponentiation operators or recursion. However, the provided solution with the loop is a valid and effective approach to solve the problem.

Overall, the `power` function correctly calculates the value of `a` to the power `b` and can be used to solve problems involving exponentiation.

Note: The provided solution assumes that `a` and `b` are non-negative integers. If you need to handle floating-point numbers or negative numbers, additional considerations may be needed to ensure the correctness of the calculation.

Here's a sample usage of the `power` function to demonstrate its usage:
```python
print(power(2, 3))  # Output: 8
print(power(5, 2))  # Output: 25
```
In these examples, the `power` function is called with different values for `a` and `b`, and the results are printed to the console. The first call calculates 2 raised to the power of 3, which is 8. The second call calculates 5 raised to the power of 2, which is