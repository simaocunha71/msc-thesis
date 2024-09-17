```
def count(lst):
    return sum(1 for x in lst if x)
```


The function `count` takes a list `lst` as an argument and returns the number of `True` values in the list. It uses a generator expression inside the `sum` function to iterate over the list and count the number of `True` values. The `assert` statement checks that the function returns the correct result for the given list `[True,False,True]`. 

For example, if the list is `[True,False,True]`, the function will return `2` because there are two `True` values in the list. The unit test `assert count([True,False,True]) == 2` ensures that the function behaves correctly for this specific input. 

The `sum` function is used to count the number of `True` values because `True` is equivalent to `1` and `False` is equivalent to `0` in a boolean context. Therefore, the sum of the boolean values in the list is the number of `True` values. 

This function assumes that the input list only contains boolean values (`True` or `False`). If the list can contain other types of values, additional error checking may be necessary. 





