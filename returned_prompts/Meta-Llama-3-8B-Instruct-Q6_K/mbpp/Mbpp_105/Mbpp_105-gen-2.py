```
def count(lst):
    return sum(1 for x in lst if x)
```


This function uses a generator expression to iterate over the list and sum up the number of True values. The `if x` part of the expression filters out the False values, so only the True values are counted. The `sum` function then adds up these counts to give the total number of True values in the list.