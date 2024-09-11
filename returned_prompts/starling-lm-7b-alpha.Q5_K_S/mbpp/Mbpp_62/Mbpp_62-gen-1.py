Here's one way to do it:

```python
def smallest_num(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
```

Explanation:
The function `smallest_num` takes a list of numbers as its input. It initializes the variable `min_num` to the first number in the list. Then, it iterates over each number in the list. If a number is smaller than the current `min_num`, it updates `min_num` to that number. Finally, it returns the smallest number found.

The `assert smallest_num([10, 20, 1, 45, 99]) == 1` line is a way to check if the function is working correctly. It asserts that when the function is called with the list `[10, 20, 1, 45, 99]`, the returned value should be `1`. If the assertion is false, an error will be raised.

This solution assumes that the input list is non-empty and contains only numeric values. If you need to handle empty lists or non-numeric values, you may need to add additional error checking.

```python
def smallest_num(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input list must contain only numeric values")
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
```

In this updated version, the function first checks if the input list is empty. If it is, it raises a `ValueError` with an appropriate error message. Then, it checks if all elements in the list are numeric by using a generator expression with the `isinstance` function. If any element is not a numeric value, it raises a `ValueError`. Finally, it proceeds with finding the smallest number as in the previous solution.

By adding these error checks, the function becomes more robust and can handle a wider