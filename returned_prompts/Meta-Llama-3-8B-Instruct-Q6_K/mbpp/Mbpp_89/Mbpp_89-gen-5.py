```
def closest_num(n):
    if n == 0:
        return -1
    for i in range(n-1, -1, -1):
        if i < n:
            return i
    return -1
```


In this function, we start from the number before `n` and move backwards until we find a number that is smaller than `n`. If we reach `0` and haven't found a smaller number, we return `-1` as there is no smaller number. This function passes the given unit test. 

Note: This function returns the first smaller number it finds, which is not necessarily the closest smaller number. For example, if the input is `11`, the function returns `10`, which is not necessarily the closest smaller number if there are other smaller numbers before `10`. If you need to find the closest smaller number, you would need a different approach.