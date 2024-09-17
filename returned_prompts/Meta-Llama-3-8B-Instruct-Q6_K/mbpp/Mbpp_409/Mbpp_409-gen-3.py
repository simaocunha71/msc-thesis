```
def min_product_tuple(lst):
    return min(a*b for a, b in lst)
```


In this function, we use a generator expression to multiply each pair of numbers in the list, and then use the built-in `min` function to find the smallest product. The unit test provided ensures that this function works correctly. 

For example, when we call `min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])`, it returns `8`, which is the smallest product of the pairs in the list. 

This function assumes that the input list contains tuples of exactly two elements each. If the list can contain tuples with more or fewer elements, you may need to add error checking code to handle this. 





This function is case-insensitive, it will return the minimum product regardless of the order of the tuples in the list. If you want a case-sensitive solution, you can use a list comprehension instead of a generator expression:

```
def min_product_tuple(lst):
    return min([a*b for a, b in lst])
```


This function is also not robust against empty input lists. If the input list is empty, it will raise an exception. If you want a robust solution, you can add a check for an empty list:

```
def min_product_tuple(lst):
    if not lst:
        return None
    return min(a*b for a, b in lst)
```


In this version, if the input list is empty, the function will return `None` instead of raising an exception.