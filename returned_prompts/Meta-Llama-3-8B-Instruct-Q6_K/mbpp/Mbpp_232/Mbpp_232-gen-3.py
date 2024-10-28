```
def larg_nnum(lst, n):
    return sorted(lst, reverse=True)[:n]
```


The unit test provided suggests that the function should return the n largest items from the list. The unit test is:
```
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
```

This unit test is saying that when the input list is [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100] and n is 2, the output should be [100, 90]. 

The function `larg_nnum` can be implemented by sorting the input list in descending order and then returning the first n items. Here's the implementation:
```
def larg_nnum(lst, n):
    return sorted(lst, reverse=True)[:n]
```
This function works by first sorting the input list in descending order using the `sorted` function with the `reverse=True` argument. This gives us a list of the n largest items. Then, we use slicing to return the first n items of the sorted list. The `[:n]` part of the code is used to get the first n items of the list. 

For example, if the input list is [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100] and n is 2, the output will be [100, 90], which is the correct result according to the unit test. 