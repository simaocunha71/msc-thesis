```
def sequential_search(arr, elem):
    for i, x in enumerate(arr):
        if x == elem:
            return (True, i)
    return (False, -1)
```


The function takes in a list `arr` and an element `elem` as inputs. It iterates over the list using the `enumerate` function, which returns both the index `i` and the value `x` of each element. If the element `elem` is found, it returns a tuple containing `True` and the index `i`. If the element is not found after iterating over the entire list, it returns a tuple containing `False` and `-1`. The unit test `assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)` ensures that the function works correctly. 

This function has a time complexity of O(n), where n is the length of the input list, because it has to iterate over the entire list in the worst case. It is not suitable for large lists. For large lists, a more efficient algorithm such as binary search or hash table lookup would be more suitable. 

However, for small to medium-sized lists, this function is simple and easy to understand, making it a good choice for small lists. It is also a good choice when the list is not sorted, as binary search requires a sorted list. 