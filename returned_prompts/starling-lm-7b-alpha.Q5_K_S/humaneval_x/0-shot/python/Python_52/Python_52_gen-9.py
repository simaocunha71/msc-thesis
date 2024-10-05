
To determine if all numbers in the list `l` are below the threshold `t`, you can follow these steps:

1. Initialize a variable `below_threshold` to `True`. This variable will keep track of whether all numbers in the list are below the threshold.

2. Iterate through each number `n` in the list `l`. For each number, check if it is less than the threshold `t`. If `n` is greater than or equal to `t`, set the `below_threshold` variable to `False` and break out of the loop.

3. If the loop completes without setting `below_threshold` to `False`, all numbers in the list are below the threshold, and the function should return `True`. Otherwise, it should return `False`.

Here's an example implementation of the `below_threshold` function:

```python
def below_threshold(l: list, t: int):
    below_threshold = True
    for n in l:
        if n >= t:
            below_threshold = False
            break
    return below_threshold
```

You can test the function using the provided test cases:

```python
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))  # Expected output: False
```

In the first test case, all numbers in the list `[1, 2, 4, 10]` are below the threshold of `100`, so the function returns `True`. In the second test case, the number `20` in the list `[1, 20, 4, 10]` is greater than or equal to the threshold of `5`, so the function returns `False`.

By following these steps and using the provided code, you can determine if all numbers in a list are below a given threshold.

```python
def below_threshold(l: list, t: int):
    below_threshold = True
    for n in l:
        if n >= t:
            below_threshold = False
            break
    return below_threshold
