```python
def median(l):
    l = sorted(l)
    n = len(l)
    if n % 2 == 1:
        return l[n//2]
    else:
        return (l[n//2 - 1] + l[n//2]) / 2
```



Explanation:

1. The `median` function takes a list `l` as input.
2. It first sorts the list `l` using the `sorted` function.
3. It then checks if the length of the list `l` is odd or even.
4. If the length is odd, it returns the middle element of the sorted list, which is the median.
5. If the length is even, it returns the average of the two middle elements of the sorted list, which is also the median.
6. The function uses integer division (`//`) to get the index of the middle element(s) in the list.

Note: The `median` function assumes that the input list `l` is not empty. If the input list is empty, the function will raise a `ZeroDivisionError` when trying to calculate the median. You may want to add a check for this case and return a default value, such as `None`, if the input list is empty.