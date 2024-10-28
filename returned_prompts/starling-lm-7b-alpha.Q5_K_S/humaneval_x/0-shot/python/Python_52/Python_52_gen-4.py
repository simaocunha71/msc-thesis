
To determine if all the numbers in a list `l` are below a certain threshold `t`, you can follow these steps:

1. Initialize a variable `result` to `True`. This variable will keep track of whether all numbers in the list are below the threshold.

2. Iterate through each number `n` in the list `l`. For each iteration, compare the number `n` with the threshold `t`. If `n` is not less than `t`, set `result` to `False` and break out of the loop. This means that at least one number in the list is not below the threshold.

3. If the loop completes without finding any number greater than or equal to the threshold, the variable `result` will still be `True`. In this case, return `True` to indicate that all numbers in the list are below the threshold.

4. If the loop is broken out of due to finding a number greater than or equal to the threshold, return `False` to indicate that not all numbers in the list are below the threshold.

Here's the code implementation of the solution:

```python
def below_threshold(l: list, t: int) -> bool:
    result = True
    for n in l:
        if n >= t:
            result = False
            break
    return result
```

You can test the function with the provided examples to verify its correctness:

```python
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))  # False
```

The first example returns `True` because all numbers in the list `[1, 2, 4, 10]` are less than the threshold `100`. The second example returns `False` because the number `20` in the list `[1, 20, 4, 10]` is greater than or equal to the threshold `5`.

By following these steps and using the provided code implementation, you can determine if all numbers in a list are below a certain threshold.

```python
def below_threshold(l: list, t: int) -> bool:
