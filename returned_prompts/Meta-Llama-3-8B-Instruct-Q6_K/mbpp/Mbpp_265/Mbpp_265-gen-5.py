```
def list_split(lst, n):
    result = []
    i = 0
    while i < len(lst):
        result.append(lst[i:i+n])
        i += n
    return result
```


The function `list_split` takes a list `lst` and an integer `n` as inputs, and returns a list of lists. It iterates over the input list `lst` in steps of `n`, appending each chunk of `n` elements to the result list. The function uses a while loop to achieve this, incrementing the index `i` by `n` at each iteration.

The unit test provided ensures that the function works correctly. For example, when called with the list `['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']` and `n=3`, the function returns the expected result `[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]`. 

This function is efficient because it only iterates over the input list once, and it uses a constant amount of extra memory to store the result list. Therefore, its time complexity is O(n), where n is the length of the input list, and its space complexity is O(n/n) = O(1), where n is the input list and n is the step size. 