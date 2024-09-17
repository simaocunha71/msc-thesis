```
def first_odd(lst):
    for num in lst:
        if num % 2 != 0:
            return num
```
This function iterates over the list of numbers. If it finds a number that is not divisible by 2 (i.e., an odd number), it returns that number. If the function finishes iterating over the list without finding an odd number, it will return None.

However, the problem statement asks for the first odd number, so we need to modify the function to return the first odd number it encounters. This is why we use the `return` statement instead of `print`.

The unit test `assert first_odd([1,3,5]) == 1` helps to clarify the problem. It suggests that the function should return the first odd number it encounters, which in this case is 1. If we used `print` instead of `return`, the function would print all the odd numbers in the list, which is not what the problem asks for.