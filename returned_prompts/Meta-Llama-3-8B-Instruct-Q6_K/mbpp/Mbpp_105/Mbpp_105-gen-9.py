```
def count(lst):
    return sum(1 for x in lst if isinstance(x, bool) and x)
```


Explanation:
The provided unit test `assert count([True,False,True]) == 2` suggests that the function should count the number of `True` values in the list. 

The function `count` iterates over each element in the list. It checks if the element is a boolean using `isinstance(x, bool)` and if it is `True`. If both conditions are met, it adds 1 to the count. The `sum` function is used to calculate the total count. The generator expression `(1 for x in lst if isinstance(x, bool) and x)` iterates over the list, checks the conditions, and yields 1 for each `True` boolean. The `sum` function then adds up these 1s to give the total count of `True` booleans.  If the element is not a boolean or is `False`, the generator expression yields 0, which is ignored by the `sum` function.  Therefore, the function correctly counts the number of `True` booleans in the list. 