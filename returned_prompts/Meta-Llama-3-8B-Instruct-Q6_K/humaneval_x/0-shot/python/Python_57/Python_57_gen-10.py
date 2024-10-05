```
def monotonic(l: list):
    if not l:
        return True

    inc = dec = True

    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            dec = False
        elif l[i] < l[i-1]:
            inc = False

    return inc or dec
```
This function checks if the list is monotonically increasing or decreasing by iterating over the list and comparing each element with its predecessor. It initializes two flags `inc` and `dec` to `True` initially, which means the list can be either increasing or decreasing. Then it iterates over the list, updating these flags based on the comparison of adjacent elements. If the list is monotonically increasing, `inc` will remain `True` and `dec` will become `False`. Similarly, if the list is monotonically decreasing, `dec` will remain `True` and `inc` will become `False`. Finally, it returns `True` if the list is either increasing or decreasing, and `False` otherwise. If the input list is empty, it returns `True` as an empty list is considered monotonically increasing and decreasing. 