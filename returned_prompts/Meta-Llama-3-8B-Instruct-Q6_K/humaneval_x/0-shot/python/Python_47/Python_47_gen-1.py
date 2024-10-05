Here is the solution:

```python
def median(l: list):
    l.sort()
    n = len(l)
    if n % 2 == 1:
        return l[n // 2]
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2
```

This function first sorts the list. Then, it checks if the length of the list is odd or even. If it's odd, it returns the middle element. If it's even, it returns the average of the two middle elements. This is because the median of a list of even length is the average of the two middle elements. 

For example, if the list is [3, 1, 2, 4, 5], the median is 3, which is the middle element. If the list is [-10, 4, 6, 1000, 10, 20], the median is 15.0, which is the average of the two middle elements 10 and 15. 

The time complexity of this function is O(n log n) due to the sorting operation. The space complexity is O(1) as it only uses a constant amount of space. 