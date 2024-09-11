Here is one way to solve this problem:

```python
def next_Perfect_Square(n):
    x = n + 1
    while True:
        if x ** 0.5 == int(x ** 0.5):
            return x
        x += 1
```

Explanation:

The function `next_Perfect_Square` takes a number `n` and returns the next perfect square greater than `n`.

In the function, we initialize a variable `x` with `n + 1`. We then enter a while loop that will continue indefinitely until we find a perfect square.

Inside the loop, we check if `x` squared is equal to its integer square root. If it is, then `x` is a perfect square and we return it. Otherwise, we increment `x` by 1 and continue the loop.

This process continues until we find the next perfect square greater than the input number `n`.

In the provided example, when we call `next_Perfect_Square(35)`, it will return `36` because the next perfect square greater than `35` is `36`.

Note: It's important to keep in mind that this function will only work correctly if the input number `n` is already a perfect square. If `n` is not a perfect square, the function will return the next perfect square, but it may not be greater than `n`.

Additionally, it's worth mentioning that the function uses the `**` operator for exponentiation and the `int()` function to convert a number to an integer.

Overall, the provided solution is a simple and efficient way to find the next perfect square greater than a given number in Python.

```python
def next_Perfect_Square(n):
    x = n + 1
    while True:
        if x ** 0.5 == int(x ** 0.5):
            return x
        x += 1
```

This Python function can be used to find the next perfect square greater than a given number. It initializes a variable `x` with the input number `n` plus one, and then enters a while loop that will continue until a perfect square is found. Inside the