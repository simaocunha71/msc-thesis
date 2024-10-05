
To determine if all numbers in a list are below a certain threshold, you can use the following function:

```python
def below_threshold(l: list, t: int) -> bool:
    for num in l:
        if num >= t:
            return False
    return True
```

In this function, the parameter `l` represents the list of numbers, and the parameter `t` represents the threshold. The function iterates through each number in the list using a `for` loop. If any number is greater than or equal to the threshold, the function immediately returns `False`, indicating that not all numbers in the list are below the threshold. If the loop completes without encountering any number greater than or equal to the threshold, the function returns `True`, indicating that all numbers in the list are below the threshold.

To test the function, you can use the following code:

```python
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))  # Output: False
```

The first test case `below_threshold([1, 2, 4, 10], 100)` returns `True` because all numbers in the list are below the threshold of 100. The second test case `below_threshold([1, 20, 4, 10], 5)` returns `False` because the number 20 is greater than or equal to the threshold of 5.

By using this function, you can easily check if all numbers in a list are below a given threshold.

```python
def below_threshold(l: list, t: int) -> bool:
    for num in l:
        if num >= t:
            return False
    return True
```

```python
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))  # Output: False
```

I hope this helps! Let me know if you have any