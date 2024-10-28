Here is the Python solution:
```
def common(l1, l2):
    return sorted(set(l1) & set(l2))
```


Explanation:
The function `common` takes two lists `l1` and `l2` as input. It first converts the lists to sets using the `set` function. The `&` operator is used to find the intersection of the two sets, which gives us the common elements. Finally, it sorts the common elements using the `sorted` function and returns the result. The `set` function automatically removes duplicates, so we don't need to use the `list(set())` trick to remove duplicates. The `sorted` function is used to sort the common elements in ascending order. The function returns a list of common elements in sorted order.