```
def pos_count(lst):
    return sum(1 for x in lst if x > 0)
```
This function uses a generator expression to iterate over the list, and counts the number of elements that are greater than 0. The `sum` function is used to add up the counts. This function passes the given unit test:
```
assert pos_count([1,-2,3,-4]) == 2
```



