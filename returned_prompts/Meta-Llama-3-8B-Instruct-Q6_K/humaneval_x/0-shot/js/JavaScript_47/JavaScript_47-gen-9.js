```python
def median(l):
    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
```
Explanation:
The median is the middle value of a sorted list. If the list has an even number of elements, the median is the average of the two middle values. If the list has an odd number of elements, the median is the middle value.

The function `median` takes a list `l` as input, sorts it, and then checks if the length of the list is even or odd.

If the length is even, it calculates the median as the average of the two middle values. If the length is odd, it returns the middle value.

Note: The problem description is missing a detail, which is that the list is a list of integers. However, this is not a significant issue, as the median function will still work correctly for a list of integers.