```
def check_greater(arr, num):
    for i in arr:
        if i > num:
            return False
    return True
```


The problem is asking you to create a function called `check_greater` that takes two parameters: an array of numbers and a single number. The function should check if the given number is greater than all the numbers in the array. If it finds a number in the array that is greater than the given number, it should return `False`. If it doesn't find any such number, it should return `True`.

The unit test `assert check_greater([1, 2, 3, 4, 5], 4) == False` helps to clarify the problem. It shows that the function should return `False` when the given number (4) is not greater than all the numbers in the array.

Here is a Python solution for the problem:

```
def check_greater(arr, num):
    for i in arr:
        if i > num:
            return False
    return True
```

This function iterates over each number in the array. If it finds a number that is greater than the given number, it immediately returns `False`. If it doesn't find any such number, it returns `True` after checking all the numbers in the array.