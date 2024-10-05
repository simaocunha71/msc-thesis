Here is a Python solution using a simple loop:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] < threshold:
            return True
    return False
```

This solution works by sorting the list of numbers, then iterating through the sorted list and checking if the difference between the current number and the next number is less than the threshold. If it is, the function returns `True`. If the function finishes iterating through the list without finding two numbers that are closer than the threshold, it returns `False`.

Please note that this function will return `True` if any two numbers in the list are closer than the threshold, not necessarily consecutive. If you want to check only for consecutive numbers, you would need to slightly modify the function.
