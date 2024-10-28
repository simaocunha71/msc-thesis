```
def zero_count(arr):
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
    non_zero_count = len(arr) - zero_count
    return zero_count / non_zero_count if non_zero_count > 0 else 0
```


This function iterates over the input array, counting the number of zeroes. It then calculates the ratio of zeroes to non-zeroes by dividing the count of zeroes by the count of non-zeroes. If there are no non-zeroes, it returns 0 (since division by zero is undefined). The `math.isclose` function from the unit test ensures that the ratio is close to 0.181818, which is the expected result for the given input array.