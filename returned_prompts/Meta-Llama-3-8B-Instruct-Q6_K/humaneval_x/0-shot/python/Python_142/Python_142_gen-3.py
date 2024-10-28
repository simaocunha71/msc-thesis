Here is a Python function that implements the described behavior:

```
def sum_squares(lst):
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total += num ** 3
    return total
```

This function uses the `enumerate` function to iterate over the list with both the index and the value of each element. It then checks the index modulo 3 and 4 to determine whether to square or cube the element. The total sum is then returned. 

The time complexity of this function is O(n), where n is the length of the input list, as it iterates over the list once. The space complexity is O(1), as it uses a constant amount of space to store the total sum. 