The task is to find a median of a list of numbers. If the list length is even, the median is the average of the two middle numbers. If it's odd, the median is the middle number.

To solve this problem, you can sort the list in ascending order, then if the length of the list is even, calculate the average of the two middle numbers. If it's odd, return the middle number.

Here is the Python code implementing this:

```python
def median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]
```

And here's how you can use it:

```python
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This code sorts the list in ascending order, then calculates the median. If the length of the list is even, it calculates the average of the two middle numbers. If it's odd, it returns the middle number.

The time complexity of this code is O(n log n) because of the sorting operation, where n is the length of the list