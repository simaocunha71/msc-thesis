```
def monotonic(l: list):
    increasing = True
    decreasing = True

    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            decreasing = False
        elif l[i] < l[i-1]:
            increasing = False

    return increasing or decreasing
```


In this solution, we initialize two boolean variables, `increasing` and `decreasing`, to `True`. This is because we want to check if the list is either monotonically increasing or decreasing.

We then iterate through the list, starting from the second element (index 1). For each element, we check if it is greater than the previous element. If it is, we set `decreasing` to `False`, because the list is not decreasing. If it is less than the previous element, we set `increasing` to `False`, because the list is not increasing.

At the end of the iteration, we return `increasing` or `decreasing`, whichever is `True`. This is because if the list is either increasing or decreasing, at least one of these conditions will be `True`. If neither condition is `True`, then the list is neither increasing nor decreasing, and we return `False`.