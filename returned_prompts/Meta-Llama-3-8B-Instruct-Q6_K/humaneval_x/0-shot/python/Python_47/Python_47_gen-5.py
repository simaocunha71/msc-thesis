The median is the middle value of a sorted list of numbers. If the list has an even number of elements, the median is the average of the two middle values. This function will return the median of the input list.

Here is the Python solution:
```
def median(l: list):
    l.sort()
    n = len(l)
    if n % 2 == 1:
        return l[n//2]
    else:
        return (l[n//2 - 1] + l[n//2]) / 2
```
This function first sorts the input list `l`. Then it checks if the length of the list `n` is odd or even. If `n` is odd, the median is the middle value of the list, which is `l[n//2]`. If `n` is even, the median is the average of the two middle values `l[n//2 - 1]` and `l[n//2]`, which are divided by 2.0 to ensure a floating point result.