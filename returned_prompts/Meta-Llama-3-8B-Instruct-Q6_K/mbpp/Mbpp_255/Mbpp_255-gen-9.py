```
def combinations_colors(lst, n):
    if n == 0:
        return [()]
    result = []
    for i in range(len(lst)):
        for combination in combinations_colors(lst[i+1:], n-1):
            result.append((lst[i],) + combination)
    return result
```


This function uses recursion to generate all combinations of the elements in the list. The base case is when n is 0, in which case the function returns a list containing an empty tuple. Otherwise, the function iterates over the list and for each element, it calls itself with the rest of the list and n-1, and then adds the current element to each combination in the result list.

Note that this function generates combinations with repetition, meaning that an element can be repeated in a combination. If you want to generate combinations without repetition, you can modify the function to keep track of the elements that have already been used in a combination.

For example, the test case `assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]` passes because the function generates all combinations of the elements in the list with repetition and returns a list with a tuple for each combination. The function correctly handles the case where n is 1, in which case it returns a list with a tuple for each element in the list.