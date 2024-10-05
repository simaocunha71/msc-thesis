The median is the middle value of the list when it is sorted in ascending order. If the list has an even number of elements, the median is the average of the two middle values.

Here is the Python solution for the problem:

```python
def median(l):
    l.sort()
    n = len(l)
    if n % 2 == 1:
        return l[n // 2]
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2
```

This function first sorts the list in ascending order. Then it checks if the length of the list is odd or even. If the length is odd, it returns the middle value. If the length is even, it returns the average of the two middle values.