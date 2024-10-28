```
def count_X(t, element):
    return t.count(element)
```
This function uses the built-in count method of the tuple class, which returns the number of occurrences of the specified element in the tuple. The function takes two parameters: the tuple `t` and the element `element` to be counted. It then returns the count of the element in the tuple. 

For example, if we call `count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4)`, the function will return `0` because the element `4` is not present in the tuple. 

The unit test `assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0` also verifies that the function returns the correct count for the given tuple and element. 