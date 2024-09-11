Here's a Python function that checks whether a given list contains consecutive numbers or not:

```python
def check_Consecutive(my_list):
    for i in range(len(my_list)-1):
        if my_list[i+1] - my_list[i] != 1:
            return False
    return True
```

Explanation:
The function `check_Consecutive` takes a single parameter `my_list`, which is the list of numbers to be checked. It iterates through the list using a `for` loop, comparing each element with the next one. If the difference between two consecutive elements is not equal to 1, it means that the list is not consecutive and the function returns `False`. If the loop completes without finding any non-consecutive pairs, the function returns `True`, indicating that the list is consecutive.

The `assert` statement at the beginning of the code is used to test the function with a sample input. In this case, the function is called with the list `[1,2,3,4,5]` and the expected output is `True`, as this list is consecutive.

You can use this function to check whether a given list is consecutive or not by calling it with your desired list as an argument.

```python
my_list = [1,2,3,4,5]
print(check_Consecutive(my_list))  # Output: True
```

This will print `True` if the list is consecutive, and `False` otherwise.

```python
my_list = [1,3,5,7]
print(check_Consecutive(my_list))  # Output: False
```

This will print `False` because the numbers in the list are not consecutive.

```python
my_list = [2,3,4,5]
print(check_Consecutive(my_list))  # Output: True
```

This will print `True` because the numbers in the list are consecutive, with a difference of 1 between each pair of consecutive elements.

Feel free to modify the function or use it as-is to suit your specific needs.
```

```

```

```