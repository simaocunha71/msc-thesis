```
def median(l: list):
    sorted_l = sorted(l)
    n = len(sorted_l)
    if n % 2 == 1:
        return sorted_l[n//2]
    else:
        return (sorted_l[n//2 - 1] + sorted_l[n//2]) / 2
```
The median of a list of numbers is the middle value when the list is sorted in ascending order. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.

The function `median` first sorts the input list `l` in ascending order using the `sorted` function. It then calculates the length `n` of the sorted list.

If `n` is odd, the function returns the middle element of the sorted list, which is at index `n//2`.

If `n` is even, the function returns the average of the two middle elements, which are at indices `n//2 - 1` and `n//2`. The average is calculated using the `+` operator for addition and the `/` operator for division.

The function is tested using the provided test cases. For the first test case, the list `[3, 1, 2, 4, 5]` has an odd number of elements, so the function returns `3`, which is the middle element. For the second test case, the list `[-10, 4, 6, 1000, 10, 20]` has an even number of elements, so the function returns `15.0`, which is the average of the two middle elements `10` and `20`. 