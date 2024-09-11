```
def is_num_decagonal(n):
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return False
    decagonal_nums = [27, 100]
    while len(decagonal_nums) < n:
        decagonal_nums.append(sum(decagonal_nums[-1: -2]) + decagonal_nums[-1] + decagonal_nums[-2] + 1)
    return decagonal_nums[n - 1]
```

Here is the Python code to solve the problem:

The `is_num_decagonal` function takes an integer `n` as input and checks if it is a valid decagonal number. A decagonal number is a number that can be represented as the sum of 10 consecutive integers, starting with 1. The function first checks if `n` is less than 1, in which case it returns `False`. Then it checks if `n` is equal to 1, in which case it returns `True`. If `n` is neither less than 1 nor equal to 1, the function checks if `n` is even. If it is, the function returns `False`. Otherwise, it initializes a list `decagonal_nums` with the first two decagonal numbers, 27 and 100. It then enters a loop that continues until the length of `decagonal_nums` is equal to `n`. In each iteration of the loop, the function appends to `decagonal_nums` the sum of the last two elements of the list, the last element of the list, and the element before the last element of the list, and adds 1. After the loop, the function returns the `n`th element of `decagonal_nums`.

To use the function, you can call it with an integer argument and check if it returns `True` or `False`. For example, `is_num_decagonal(3)` will return `True` because 3 is a valid decagonal number.

Here is a sample usage of the function:

```python
print(is_num_decagonal(3))  # True
``