```
def pair_wise(lst):
    result = []
    for i in range(len(lst)):
        if i < len(lst) - 1:
            result.append((lst[i], lst[i+1]))
    return result
```


The function pair_wise takes a list as input and returns a list of all pairs of consecutive items in the given list. 

The function iterates over the list using a for loop and for each item, it appends a tuple containing the current item and the next item in the list to the result list. 

If the current item is the last item in the list, it does not append anything to the result list, as there is no next item. 

Finally, the function returns the result list. 

The unit test `assert pair_wise([1,1,2,3,3,4,4,5]) == [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]` ensures that the function works correctly for a list with duplicate elements.  The test checks if the function returns all pairs of consecutive items in the list, including pairs with duplicate elements. 

This function works correctly even if the list has duplicate elements or if the list is empty.  For example, `pair_wise([1,1,2,3,3,4,4,5])` returns `[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]` and `pair_wise([])` returns `[]`.  If the list has less than two elements, the function returns an empty list.  For example, `pair_wise([1])` returns `[]` and `pair_wise([1,2])` returns `[(1, 2)]`.  In general, the function correctly handles all possible inputs.  It does not modify the input list and it returns a new list.  The returned list is a copy of the input list and it can be modified independently of the input list.  The function does not use any external variables or functions and it does not have any side effects.  It is a pure function.  The function is simple and easy to understand, and it is easy to test.  It is a good example of