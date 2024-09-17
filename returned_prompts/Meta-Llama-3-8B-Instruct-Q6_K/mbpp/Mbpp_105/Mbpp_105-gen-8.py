```
def count(lst):
    return sum(1 for x in lst if x)
```


The given function `count` takes a list `lst` as an argument and returns the number of `True` values in the list. This is achieved by using a generator expression inside the `sum` function. The expression `1 for x in lst if x` iterates over the list and yields 1 for each element that is `True`. The `sum` function then adds up these 1s to give the total number of `True` values in the list. 

The unit test `assert count([True,False,True]) == 2` ensures that the function correctly returns the count of `True` values in the list. In this case, the function should return 2, because there are two `True` values in the list. 





