Here's the implementation for the sum_squares function:

```python
def sum_squares(lst):
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num ** 2
        elif i % 4 == 0:
            total += num ** 3
        else:
            total += num
    return total
```

The function iterates over the list using enumerate to get both the index and the value of each element. It then checks if the index is a multiple of 3 or 4, and performs the corresponding operation on the value. Finally, it returns the sum of all the modified values.