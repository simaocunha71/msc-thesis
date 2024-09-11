Here's a possible solution:

```python
def square_Sum(n):
    result = 0
    for i in range(1, 2 * n + 1, 2):
        result += i ** 2
    return result
```

This function `square_Sum` takes an integer `n` as input. It initializes a variable `result` to 0. Then, using a `for` loop, it iterates over the range of odd numbers from 1 to `2 * n + 1` (inclusive) with a step size of 2. For each odd number `i`, it calculates the square of `i` using the `**` operator and adds it to the `result`. Finally, it returns the `result`.

To verify that the function works correctly, you can use the `assert` statement to check if the result of `square_Sum(2)` is equal to 10. If the assertion passes, it means that the function is working as expected.

Here's an example usage of the function:

```python
print(square_Sum(2))  # Output: 10
```

In this example, we pass the argument `2` to the `square_Sum` function, which calculates the sum of squares of the first 2 odd natural numbers (1 and 3) and returns the result, which is 10.

I hope this helps! Let me know if you have any further questions.
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

``