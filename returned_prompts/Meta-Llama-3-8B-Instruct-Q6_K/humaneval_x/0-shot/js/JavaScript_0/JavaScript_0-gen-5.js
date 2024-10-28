Here is the Python function to solve the problem:

```Python
def hasCloseElements(numbers, threshold):
    numbers = sorted(numbers)
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i+1]) < threshold:
            return True
    return False
```

The function `hasCloseElements` takes a list of numbers and a threshold as input. It first sorts the list of numbers. Then it iterates over the sorted list, checking if the absolute difference between two consecutive numbers is less than the threshold. If it finds such a pair, it immediately returns `True`. If it doesn't find any such pair after checking all pairs, it returns `False`. 

For example, `hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)` returns `True` because the difference between `2.0` and `2.8` is less than `0.3`. On the other hand, `hasCloseElements([1.0, 2.0, 3.0], 0.5)` returns `False` because no two numbers in the list are closer than `0.5`. 