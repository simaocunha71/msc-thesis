Here is a possible implementation of the function:

```python
def sum_squares(lst):
    total = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            total += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total += lst[i] ** 3
        else:
            total += lst[i]
    return total
```

You can test the function with the provided examples:

```python
print(sum_squares([1,2,3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1,-5,2,-1,-5]))  # Output: -126
```