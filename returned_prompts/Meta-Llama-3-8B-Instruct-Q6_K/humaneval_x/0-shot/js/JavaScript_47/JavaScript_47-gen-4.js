```python
def median(l):
    sorted_list = sorted(l)
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n//2]
    else:
        return (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
```



Python code that defines a function `median` that calculates the median of a list of numbers. The function first sorts the list, then checks if the length of the list is odd or even. If the length is odd, the median is the middle element. If the length is even, the median is the average of the two middle elements.

The unit tests provided in the problem statement are:
```
>>> median([3, 1, 2, 4, 5])
3
>>> median([-10, 4, 6, 1000, 10, 20])
8.0
```

The first test case checks if the median of the list `[3, 1, 2, 4, 5]` is `3`, which is correct.

The second test case checks if the median of the list `[-10, 4, 6, 1000, 10, 20]` is `8.0`, which is also correct.

The median function works by first sorting the list of numbers, then finding the middle element(s) and calculating the median accordingly. This approach ensures that the median is calculated correctly for both odd and even length lists.