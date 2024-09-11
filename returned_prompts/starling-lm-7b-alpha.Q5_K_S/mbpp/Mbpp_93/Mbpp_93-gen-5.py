```
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
```

Explanation:

The function `power` calculates the value of `a` raised to the power `b`. It uses a recursive approach to calculate the result. 

In the function, we check if `b` is equal to 0. If it is, we return 1, as any number raised to the power of 0 is 1. 

If `b` is not equal to 0, we multiply `a` by the result of `power(a, b - 1)`. Here, `power(a, b - 1)` calculates the value of `a` raised to the power `b - 1`. 

By recursively calling the `power` function with decreasing values of `b`, we eventually reach the base case of `b` being 0, and the function returns the final result.

In the example `power(3, 4)`, the function is called with `a = 3` and `b = 4`. It follows the recursive steps to calculate `3 * 3 * 3 * 3`, which equals 81. 

The assert statement checks if the calculated result matches the expected result of 81, ensuring the correctness of the function.

Overall, the `power` function provides a way to calculate the value of `a` raised to the power `b` using recursion.

```python
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
```

The above code defines a function called `power` that takes in two parameters `a` and `b`. It uses recursion to calculate the value of `a` raised to the power `b`. 

In the function, we first check if `b` is equal to 0. If it is, we return 1, as any number raised to the power of 0 is 1. 

If `b` is not equal to 0, we multiply `a` by the result of `power(a