```
def pair_wise(lst):
    result = []
    for i in range(len(lst)):
        if i < len(lst) - 1:
            result.append((lst[i], lst[i+1]))
    return result
```


Explanation:
The function `pair_wise` takes a list `lst` as input and returns a list of all pairs of consecutive items in the list. It does this by iterating over the list using a for loop, and for each item, it appends a tuple of the current item and the next item to the result list. The if condition `i < len(lst) - 1` is used to avoid an IndexError when trying to access the next item in the list. The function then returns the result list. 

For example, if the input list is `[1,1,2,3,3,4,4,5]`, the function will return `[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]`. 

The unit test `assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]` ensures that the function works correctly. 





```
```


Explanation:
The function `pair_wise` takes a list `lst` as input and returns a list of all pairs of consecutive items in the list. It does this by iterating over the list using a for loop, and for each item, it appends a tuple of the current item and the next item to the result list. The if condition `i < len(lst) - 1` is used to avoid an IndexError when trying to access the next item in the list. The function then returns the result list. 

For example, if the input list is `[1,1,2,3,3,4,4,5]`, the function will return `[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]`. 

The unit test `assert pair_wise([1,1,2,3,3,4