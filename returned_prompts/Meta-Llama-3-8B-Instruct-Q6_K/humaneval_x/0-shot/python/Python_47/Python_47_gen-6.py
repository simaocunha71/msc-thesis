Here is the solution using the built-in `sorted` function to sort the list and then finding the middle element:

```
def median(l: list):
    sorted_l = sorted(l)
    n = len(sorted_l)
    if n % 2 == 0:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_l[n // 2]
```

This function first sorts the input list `l` using the `sorted` function. Then it calculates the length of the list `n`. If the length is even, it calculates the two middle elements `mid1` and `mid2`, adds them and divides by 2 to get the median. If the length is odd, it returns the middle element directly. The function also handles the case where the median is not an integer by returning a floating-point number. This solution has a time complexity of O(n log n) due to the sorting operation.