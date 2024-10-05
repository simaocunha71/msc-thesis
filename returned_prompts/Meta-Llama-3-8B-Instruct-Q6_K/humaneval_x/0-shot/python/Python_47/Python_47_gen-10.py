The median is the middle value of a list when it is sorted in ascending order. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.

Here is a Python function that calculates the median of a list:

```
def median(l: list):
    l.sort()
    n = len(l)
    if n % 2 == 1:
        return l[n // 2]
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2
```

This function first sorts the list in ascending order. Then, it checks if the list has an odd or even number of elements. If it has an odd number of elements, it returns the middle element. If it has an even number of elements, it returns the average of the two middle elements. The `//` operator is used for integer division, which returns the largest whole number less than or equal to the result of the division.

For example, if you call `median([3, 1, 2, 4, 5])`, the function will return `3`, because `3` is the middle element of the sorted list `[1, 2, 3, 4, 5]`. If you call `median([-10, 4, 6, 1000, 10, 20])`, the function will return `15.0`, because `15` is the average of the two middle elements `15` and `20` of the sorted list `[-10, 4, 6, 10, 15, 20, 1000]`. 