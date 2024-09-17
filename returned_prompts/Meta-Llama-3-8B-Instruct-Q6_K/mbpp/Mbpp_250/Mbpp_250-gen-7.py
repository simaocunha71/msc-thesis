```
def count_X(t, element):
    return t.count(element)
```


This function uses the built-in `count` method of Python's list and tuple data types, which returns the number of occurrences of the specified element in the tuple. In this case, the tuple is passed as the first argument `t` and the element to be counted is passed as the second argument `element`. The function then returns the count of the element in the tuple. The unit test `assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0` ensures that the function correctly returns 0 when the element is not present in the tuple.