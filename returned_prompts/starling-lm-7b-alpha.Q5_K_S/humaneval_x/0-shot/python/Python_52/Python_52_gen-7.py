
To determine if all numbers in a given list `l` are below a specified threshold `t`, you can use the following steps:

1. Iterate through each number in the list `l`.
2. Check if the current number is below the threshold `t`. If it is, continue to the next number. If not, return `False` to indicate that not all numbers are below the threshold.
3. If all numbers have been checked and none of them are above the threshold, return `True` to indicate that all numbers are below the threshold.

Here's an example implementation of the `below_threshold` function:

```python
def below_threshold(l: list, t: int):
    for num in l:
        if num > t:
            return False
    return True
```

In this implementation, we use a `for` loop to iterate through each number in the list `l`. Inside the loop, we check if the current number (`num`) is greater than the threshold (`t`). If it is, we immediately return `False` to indicate that at least one number in the list is above the threshold. If all numbers have been checked and none of them are above the threshold, we return `True` to indicate that all numbers are below the threshold.

You can test the function with the provided examples:

```python
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))  # Expected output: False
```

The first test case passes because all numbers in the list `[1, 2, 4, 10]` are below the threshold of `100`. The second test case fails because the number `20` in the list `[1, 20, 4, 10]` is above the threshold of `5`.