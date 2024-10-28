```
def choose_num(x, y):
    if x % 2 != 0 and y % 2 != 0:
        return -1
    elif x % 2 == 0:
        return x
    elif y % 2 == 0:
        return y
    else:
        return min(x, y)
```


This function first checks if both x and y are odd. If they are, then there's no even number in the range [x, y], so the function returns -1. If x is even, then the function returns x. If y is even, then the function returns y. If neither x nor y is even, then the function returns the smaller of the two numbers, since it's the largest even number in the range.